# TODO: сделать наследование
from typing import Any, Dict, List, Type

from uuid import UUID

from fastapi import Depends
from pydantic import parse_obj_as
from pydantic.main import BaseModel

from core.settings import Settings
from src.storage.search import AsyncSearchStorage
from storage.instances.elastic.storage import get_elastic

settings = Settings()

# TODO: вынести INDEX_NAME
INDEX_NAME = "questions"


# TODO: вынести модель вопроса
class Question(BaseModel):
    id: UUID
    text: str
    tags: List[str] = []
    author: str = ""
    timestamp: str


# TODO: разнести по разным файлам
class SearchService:
    def __init__(self, search: AsyncSearchStorage):
        self.search = search

    def _hits_to_model_list(self, list_model: Type[List[BaseModel]], es_docs: Dict[str, Any]) -> List[BaseModel]:
        values_dict = [item["_source"] for item in es_docs["hits"]["hits"]]
        objs = parse_obj_as(list_model, values_dict)
        return objs


class QuestionsSearchService(SearchService):
    async def search_question(self, edsl_query: dict[str, Any]) -> List[Question]:
        return self._hits_to_model_list(
            list_model=List[Question],  # type: ignore
            es_docs=await self.search.search(index=INDEX_NAME, body=edsl_query),
        )


def get_questions_search_service(search: AsyncSearchStorage = Depends(get_elastic)) -> QuestionsSearchService:
    return QuestionsSearchService(search=search)
