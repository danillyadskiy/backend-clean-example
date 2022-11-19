from elasticsearch import AsyncElasticsearch

from business import Publication, PublicationFilters
from business.interfaces import IPublicationGateway
from core.elastic_config import KNOWLEDGE_INDEX_NAME
from gateways.elastic.converters import PublicationConverter
from gateways.elastic.schema import PublicationSchema
from gateways.elastic.services import EDSLGenerator, EDSLParser, SearchLoader


class PublicationGateway(IPublicationGateway):
    def __init__(self, search: AsyncElasticsearch):
        self.__search = search
        self.__loader = SearchLoader(self.__search)

    async def get(self, filters: PublicationFilters) -> list[Publication]:
        edsl_query = EDSLGenerator.generate_publication_text_edsl(filters.text)
        publication_schemes = EDSLParser.hits_to_model_list(
            list_model=list[PublicationSchema],
            es_docs=await self.__search.search(index=KNOWLEDGE_INDEX_NAME, body=edsl_query),
        )
        return PublicationConverter.list_to_business(publication_schemes)

    async def save(self, publication: Publication) -> None:
        publication_schema = PublicationConverter.from_business(publication)
        await self.__loader.upload_index_data(
            [{"index": {"_index": KNOWLEDGE_INDEX_NAME, "_id": publication_schema.id}}, publication_schema.dict()]
        )
