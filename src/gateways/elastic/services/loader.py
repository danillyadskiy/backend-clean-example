from typing import Any

from elasticsearch import AsyncElasticsearch


class SearchLoader:
    def __init__(self, search: AsyncElasticsearch) -> None:
        self.__search = search

    async def create_mapping(self, index_name: str, body: dict[str, Any]) -> None:
        if not await self.__search.indices.exists(index_name):
            await self.__search.indices.create(index=index_name, body=body)

    async def delete_index(self, index_name: str) -> None:
        if await self.__search.indices.exists(index_name):
            await self.__search.indices.delete(index_name)

    async def upload_index_data(self, data: list[dict[str, str]]) -> dict[str, Any]:
        return await self.__search.bulk(body=data, request_timeout=3600)
