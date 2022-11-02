from functools import lru_cache

from elasticsearch import Elasticsearch

from core.settings import Settings
from services.loader.elastic import ElasticSearchLoader
from services.search.service import KnowledgePublication
from storage.instances.elastic.settings import KNOWLEDGE_INDEX_NAME

settings = Settings()


class LoaderService:
    ...


class KnowledgePublicationsLoaderService(LoaderService):
    def __init__(self) -> None:
        self.loader = ElasticSearchLoader(Elasticsearch(hosts=[settings.elastic]))

    # TODO: надо поменять на асинхронную загрузку
    # TODO: делать проверку на errors в resp
    def upload_knowledge_publication(self, publication: KnowledgePublication) -> bool:
        request_body = [{"index": {"_index": KNOWLEDGE_INDEX_NAME, "_id": publication.id}}, publication.dict()]
        response = self.loader.upload_index_data(request_body)
        return response["errors"] is False


@lru_cache()
def get_knowledge_publications_loader_service() -> KnowledgePublicationsLoaderService:
    return KnowledgePublicationsLoaderService()
