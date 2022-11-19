from business import Publication, PublicationFilters
from business.interfaces import IPublicationGateway


class SearchPublicationsUseCase:
    def __init__(self, publication_gateway: IPublicationGateway):
        self.__publication_gateway = publication_gateway

    async def search_publications(self, filters: PublicationFilters) -> list[Publication]:
        return await self.__publication_gateway.get(filters)
