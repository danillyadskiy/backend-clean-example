# TODO: сделать наследование
from typing import Any, Dict, List, Optional, Type

from uuid import UUID

from pydantic import parse_obj_as
from pydantic.main import BaseModel

from src.storage.search import AsyncSearchStorage

# TODO: вынести INDEX_NAME
INDEX_NAME = "questions"


# TODO: вынести модель вопроса
class Question(BaseModel):
    id: UUID
    text: str
    tags: List[str] = []
    author: str = ""
    timestamp: str


class SearchService:
    def __init__(self, search: AsyncSearchStorage):
        self.search = search

    def _hits_to_model_list(
        self, list_model: Type[List[BaseModel]], es_docs: Dict[str, Any]
    ) -> Optional[List[BaseModel]]:
        values_dict = [item["_source"] for item in es_docs["hits"]["hits"]]
        objs = parse_obj_as(list_model, values_dict)
        return objs


class QuestionSearchService(SearchService):
    async def search_question(self, edsl_query: dict[str, Any]) -> Optional[List[Question]]:
        return self._hits_to_model_list(
            list_model=List[Question],  # type: ignore
            es_docs=await self.search.search(index=INDEX_NAME, body=edsl_query),
        )
