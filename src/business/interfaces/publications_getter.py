from typing import Optional

from abc import ABC, abstractmethod

from business import Publication, PublicationFilters


class IPublicationsGetter(ABC):
    @abstractmethod
    async def get(self, filters: Optional[PublicationFilters] = None) -> list[Publication]:
        ...
