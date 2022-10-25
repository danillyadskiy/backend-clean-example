from typing import Optional

from elasticsearch import AsyncElasticsearch

elastic_storage: Optional[AsyncElasticsearch] = None


# Функция понадобится при внедрении зависимостей
async def get_elastic() -> AsyncElasticsearch:
    return elastic_storage
