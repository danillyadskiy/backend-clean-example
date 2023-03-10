from typing import Optional

from elasticsearch import AsyncElasticsearch

from business import Publication, PublicationFilters
from business.interfaces import IPublicationSaver, IPublicationsGetter
from core.elastic_config import KNOWLEDGE_INDEX_NAME
from gateways.elastic.mappers import PublicationMapper
from gateways.elastic.schema import PublicationSchema
from gateways.elastic.services import EDSLGenerator, EDSLParser, SearchLoader


class PublicationGateway(IPublicationsGetter, IPublicationSaver):
    def __init__(self, search: AsyncElasticsearch):
        self.__search = search
        self.__loader = SearchLoader(self.__search)

    async def get(self, filters: Optional[PublicationFilters] = None) -> list[Publication]:
        edsl_filters = EDSLGenerator.generate_publication_filters_edsl(filters) if filters else []
        edsl_query = EDSLGenerator.generate_publication_query_edsl(edsl_filters=edsl_filters)

        publication_schemes = EDSLParser.hits_to_model_list(
            list_model=list[PublicationSchema],
            es_docs=await self.__search.search(index=KNOWLEDGE_INDEX_NAME, body=edsl_query),
        )
        return PublicationMapper.list_to_business(publication_schemes)

    async def save(self, publication: Publication) -> None:
        publication_schema = PublicationMapper.from_business(publication)
        await self.__loader.upload_index_data(
            [{"index": {"_index": KNOWLEDGE_INDEX_NAME, "_id": publication_schema.id}}, publication_schema.dict()]
        )
