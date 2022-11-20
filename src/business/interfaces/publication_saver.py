from abc import ABC, abstractmethod

from business import Publication


class IPublicationSaver(ABC):
    @abstractmethod
    async def save(self, publication: Publication) -> None:
        ...
