from pathlib import Path

from unstructured.ingest.v2.interfaces import ProcessorConfig
from unstructured.ingest.v2.logger import logger
from unstructured.ingest.v2.pipeline.pipeline import Pipeline
from unstructured.ingest.v2.processes.chunker import ChunkerConfig
from unstructured.ingest.v2.processes.connectors.local import (
    LocalConnectionConfig,
    LocalDownloaderConfig,
    LocalIndexerConfig,
    LocalUploaderConfig,
)
from unstructured.embed.voyageai import VoyageAIEmbeddingConfig, VoyageAIEmbeddingEncoder
from unstructured.ingest.v2.processes.embedder import EmbedderConfig
from unstructured.ingest.v2.processes.partitioner import PartitionerConfig

from unstructured.ingest.v2.processes.connectors.astra import (
    AstraUploaderConfig,
    AstraConnectionConfig,
    AstraAccessConfig,
    AstraUploadStagerConfig,
)
import os

from unstructured.ingest.v2.processes.embedder import EmbedderConfig
from unstructured.ingest.v2.processes.partitioner import PartitionerConfig

from dotenv import load_dotenv

# from embedderv2 import EmbedderConfig2

load_dotenv()

base_path = Path(__file__).parent.parent
print(base_path)
docs_path = base_path / "regulations"
work_dir = base_path / "work_dir"
output_path = work_dir / "output"
download_path = work_dir / "download"

Pipeline.from_configs(
    context=ProcessorConfig(work_dir=str(work_dir.resolve())),
    source_connection_config=LocalConnectionConfig(),
    indexer_config=LocalIndexerConfig(
            input_path=str(docs_path.resolve()) + "/EVS_EN_62304;2006+A1;2015_en.pdf"
        ),
    downloader_config=LocalDownloaderConfig(download_dir=download_path),
    partitioner_config=PartitionerConfig(
        strategy="fast", #"hi_res" #for  images
        api_key=os.environ["UNSTRUCTURED_API_KEY"],
        partition_by_api=True,
        partition_endpoint=os.environ["UNSTRUCTURED_PARTITION_ENDPOINT"],
        ),
    chunker_config=ChunkerConfig(chunking_strategy="by_title"),
    embedder_config=EmbedderConfig(embedding_provider="langchain-huggingface"),
    destination_connection_config=AstraConnectionConfig(
        access_config=AstraAccessConfig(
            token=os.environ["ASTRA_DB_TOKEN"], api_endpoint=os.environ["ASTRA_DB_ENDPOINT"]
        )
    ),
    stager_config=AstraUploadStagerConfig(),
    uploader_config=AstraUploaderConfig(
        collection_name=os.environ["COLLECTION_NAME"],
        embedding_dimension=int(os.environ["EMBEDDING_DIMENSION"]),
        requested_indexing_policy={"deny": ["metadata"]},
    ),
).run()
