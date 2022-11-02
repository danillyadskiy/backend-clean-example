from typing import Any, Dict, List, Type

from fastapi import Depends
from pydantic import parse_obj_as
from pydantic.main import BaseModel

from core.settings import Settings
from models.knowledge_publication import KnowledgePublication
from src.storage.search import AsyncSearchStorage
from storage.instances.elastic.settings import KNOWLEDGE_INDEX_NAME
from storage.instances.elastic.storage import get_elastic

settings = Settings()


# TODO: разнести по разным файлам
class SearchService:
    def __init__(self, search: AsyncSearchStorage):
        self.search = search

    def _hits_to_model_list(self, list_model: Type[List[BaseModel]], es_docs: Dict[str, Any]) -> List[BaseModel]:
        values_dict = [item["_source"] for item in es_docs["hits"]["hits"]]
        objs = parse_obj_as(list_model, values_dict)
        return objs


class KnowledgePublicationsSearchService(SearchService):
    async def search_publications(self, edsl_query: dict[str, Any]) -> List[KnowledgePublication]:
        return self._hits_to_model_list(
            list_model=List[KnowledgePublication],
            es_docs=await self.search.search(index=KNOWLEDGE_INDEX_NAME, body=edsl_query),
        )


def get_knowledge_publications_search_service(
    search: AsyncSearchStorage = Depends(get_elastic),
) -> KnowledgePublicationsSearchService:
    return KnowledgePublicationsSearchService(search=search)
