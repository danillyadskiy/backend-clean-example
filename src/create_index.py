# TODO: удалить src
from elasticsearch import Elasticsearch

from core.settings import Settings
from src.services.loader.elastic import ElasticSearchLoader
from storage.instances.elastic.settings import QUESTIONS_INDEX_NAME, QUESTIONS_INDEX_SETTINGS

if __name__ == "__main__":
    settings = Settings()
    es = ElasticSearchLoader(Elasticsearch(hosts=[settings.elastic]))
    es.create_mapping(index_name=QUESTIONS_INDEX_NAME, body=QUESTIONS_INDEX_SETTINGS)
    # es.delete_index(index_name=QUESTIONS_INDEX_NAME)
