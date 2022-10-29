# TODO: удалить src
from elasticsearch import Elasticsearch

from core.settings import Settings
from services.loader.elastic import ElasticSearchLoader
from storage.instances.elastic.settings import KNOWLEDGE_INDEX_NAME, KNOWLEDGE_INDEX_SETTINGS

if __name__ == "__main__":
    settings = Settings()
    es = ElasticSearchLoader(Elasticsearch(hosts=[settings.elastic]))
    es.create_mapping(index_name=KNOWLEDGE_INDEX_NAME, body=KNOWLEDGE_INDEX_SETTINGS)
    # es.delete_index(index_name=KNOWLEDGE_INDEX_NAME)
