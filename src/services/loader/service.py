from functools import lru_cache

from elasticsearch import Elasticsearch

from core.settings import Settings
from services.loader.elastic import ElasticSearchLoader
from services.search.service import Question
from storage.instances.elastic.settings import QUESTIONS_INDEX_NAME

settings = Settings()


class LoaderService:
    ...


class QuestionsLoaderService(LoaderService):
    def __init__(self) -> None:
        self.loader = ElasticSearchLoader(Elasticsearch(hosts=[settings.elastic]))

    # TODO: надо поменять на асинхронную загрузку
    # TODO: делать проверку на errors в resp
    def upload_question(self, question: Question) -> bool:
        request_body = [{"index": {"_index": QUESTIONS_INDEX_NAME, "_id": question.id}}, question.dict()]
        response = self.loader.upload_index_data(request_body)
        return response["errors"] is False


@lru_cache()
def get_questions_loader_service() -> QuestionsLoaderService:
    return QuestionsLoaderService()
