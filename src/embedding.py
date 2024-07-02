import os

import voyageai
from dotenv import load_dotenv

load_dotenv()

VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")

vo = voyageai.Client()

result = vo.embed(["hello world"], model="voyage-large-2-instruct")

documents_embeddings = vo.embed(
    texts=["hello world"], model="voyage-law-2", input_type="document"
).embeddings

print(len(documents_embeddings[0]))
