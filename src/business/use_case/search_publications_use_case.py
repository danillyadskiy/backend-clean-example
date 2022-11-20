from business import Publication, PublicationFilters
from business.interfaces import IPublicationsGetter


class SearchPublicationsUseCase:
    def __init__(self, publications_getter: IPublicationsGetter):
        self.__publications_getter = publications_getter

    async def search_publications(self, filters: PublicationFilters = None) -> list[Publication]:
        return await self.__publications_getter.get(filters)
