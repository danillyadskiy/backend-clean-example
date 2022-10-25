from typing import Any

from abc import ABC
from uuid import UUID


class AsyncSearchStorage(ABC):
    async def search(self, *args: tuple) -> Any:
        ...

    async def get(self, document_id: UUID, *args: tuple) -> Any:
        ...
