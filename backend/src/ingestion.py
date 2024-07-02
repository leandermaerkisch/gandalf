import os
from dotenv import load_dotenv
from unstructured.ingest.connector.local import SimpleLocalConfig
from unstructured.ingest.interfaces import (PartitionConfig, ProcessorConfig,
                                            ReadConfig)
from unstructured.ingest.runner import LocalRunner

load_dotenv()

if __name__ == "__main__":
    runner = LocalRunner(
        processor_config=ProcessorConfig(
            verbose=True,
            output_dir="local-ingest-output",
            num_processes=2,
        ),
        read_config=ReadConfig(),
        partition_config=PartitionConfig(
            partition_by_api=True,
            api_key=os.getenv("UNSTRUCTURED_API_KEY"),
        ),
        connector_config=SimpleLocalConfig(
            input_path="regulations",
            recursive=True,
        ),
    )
    runner.run()

#     Pipeline.from_configs(
#         context=ProcessorConfig(reprocess=True, verbose=False),
#         source_connection_config=SimpleLocalConfig(
#             input_path="regulations",
#             recursive=True,
#         ),
#         indexer_config=LocalFileConfig(
#             file_path="regulations/EVS_EN_62304;2006+A1;2015_en.pdf"
#         ),
#         partitioner_config=PartitionerConfig(
#             strategy="fast", #"hi_res" #for  images
#             api_key=os.getenv("UNSTRUCTURED_API_KEY"),
#             partition_by_api=True,
#             partition_endpoint=os.getenv("UNSTRUCTURED_PARTITION_ENDPOINT"),
#             ),
#         chunker_config=ChunkerConfig(chunking_strategy="by_title"),
#         embedder_config=EmbedderConfig(embedding_provider="langchain-huggingface"),
#         destination_connection_config=AstraConnectionConfig(
#             access_config=AstraAccessConfig(
#                 token=os.getenv("ASTRA_DB_TOKEN"), api_endpoint=os.getenv("ASTRA_DB_ENDPOINT")
#             )
#         ),
#         stager_config=AstraUploadStagerConfig(),
#         uploader_config=AstraUploaderConfig(
#             collection_name=os.getenv("COLLECTION_NAME"),
#             embedding_dimension=int(os.getenv("EMBEDDING_DIMENSION")),
#             requested_indexing_policy={"deny": ["metadata"]},
#         ),
#     ).run()

# # Pipeline.from_configs(
# #     context=ProcessorConfig(tqdm=True, reprocess=True, verbose=False),
# #     source_connection_config=LocalFileConfig(
# #         file_path="regulations/EVS_EN_62304;2006+A1;2015_en.pdf"
# #     ),
# #     indexer_config=GoogleDriveIndexerConfig(),
# #     downloader_config=GoogleDriveDownloaderConfig(),
# #     partitioner_config=PartitionerConfig(
# #         strategy="fast", #"hi_res" #for  images
# #         api_key=os.getenv("UNSTRUCTURED_API_KEY"),
# #         partition_by_api=True,
# #         partition_endpoint=os.getenv("UNSTRUCTURED_PARTITION_ENDPOINT"),
# #         ),
# #     chunker_config=ChunkerConfig(chunking_strategy="by_title"),
# #     embedder_config=EmbedderConfig(embedding_provider="langchain-huggingface"),
# #     destination_connection_config=AstraConnectionConfig(
# #         access_config=AstraAccessConfig(
# #             token=os.getenv("ASTRA_DB_TOKEN"), api_endpoint=os.getenv("ASTRA_DB_ENDPOINT")
# #         )
# #     ),
# #     stager_config=AstraUploadStagerConfig(),
# #     uploader_config=AstraUploaderConfig(
# #         collection_name=os.getenv("COLLECTION_NAME"),
# #         embedding_dimension=int(os.getenv("EMBEDDING_DIMENSION")),
# #         requested_indexing_policy={"deny": ["metadata"]},
# #     ),
# # ).run()
