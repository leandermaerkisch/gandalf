import os
import uuid
import chromadb
from chromadb.config import Settings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from astrapy import DataAPIClient
from astrapy.constants import VectorMetric
from transformers import AutoTokenizer, AutoModel
import torch
import traceback
import voyageai
import time

from dotenv import load_dotenv
load_dotenv()

collection_name = "mount_doom"
file_path = "../regulations/EVS_EN_62304;2006+A1;2015_en.pdf"
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

def get_embedding(text):
    inputs = tokenizer(text=text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy().tolist()

def get_voyage_embedding(text):
    RETRIES = 3
    tries = 0
    while RETRIES > tries:
        try:
            tries += 1
            VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")
            vo = voyageai.Client()
            embed = vo.embed(
                texts=[text], model="voyage-law-2", input_type="document"
            ).embeddings[0]
            return embed
        except:
            print("throttling, waiting 30 seconds and retrying")
            time.sleep(30)

# Initialize the client
client = DataAPIClient(os.environ["ASTRA_DB_TOKEN"])
db = client.get_database_by_api_endpoint(
  "https://0d4c3670-be80-4f20-9b32-239e33f592fb-us-east-2.apps.astra.datastax.com"
)
collection = db.create_collection(
    collection_name,
    dimension=1024,
    metric=VectorMetric.COSINE,  # or simply "cosine"
    check_exists=False,
)

print(f"Connected to Astra DB: {db.list_collection_names()}")

loader = PyPDFLoader(file_path)
document = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunked_documents = text_splitter.split_documents(document)

docs = []
for doc in chunked_documents:
    print(f"dimensions of embeddings: {len(get_voyage_embedding(doc.page_content))}")
    docs.append({
        "_id": str(uuid.uuid4()),
        "text": doc.page_content,
        "$vector": get_voyage_embedding(doc.page_content)
    })

try:
    insertion_result = collection.insert_many(docs)
    print(f"* Inserted {len(insertion_result.inserted_ids)} items.\n")
except:
    traceback.print_exc()

