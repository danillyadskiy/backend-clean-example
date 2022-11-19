from abc import ABC, abstractmethod

from business import Publication, PublicationFilters


class IPublicationGateway(ABC):
    @abstractmethod
    async def get(self, filters: PublicationFilters) -> list[Publication]:
        ...

    @abstractmethod
    async def save(self, publication: Publication) -> None:
        ...
