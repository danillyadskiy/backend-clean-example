from typing import Optional

from uuid import UUID

from pydantic import BaseModel


class PublicationSchema(BaseModel):
    id: UUID
    text: str
    tags: list[str]
    timestamp: float
    author_id: int
    author_first_name: Optional[str]
    author_last_name: Optional[str]
    author_login: str
    published_channel_id: int
    published_message_id: int
