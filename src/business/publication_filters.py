from typing import Optional

from pydantic import BaseModel


class PublicationFilters(BaseModel):
    text: Optional[str]
    tags: Optional[list[str]]
