from core.elastic_config import KNOWLEDGE_INDEX_NAME, KNOWLEDGE_INDEX_SETTINGS, es_client
from gateways.elastic.services import SearchLoader

if __name__ == "__main__":
    SearchLoader(es_client).create_mapping(index_name=KNOWLEDGE_INDEX_NAME, body=KNOWLEDGE_INDEX_SETTINGS)
