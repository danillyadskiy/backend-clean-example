from abc import ABC, abstractmethod

from business import Publication, PublicationFilters


class IPublicationsGetter(ABC):
    @abstractmethod
    async def get(self, filters: PublicationFilters = None) -> list[Publication]:
        ...
