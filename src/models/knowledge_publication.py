from typing import Optional

from uuid import UUID

from pydantic import BaseModel


class KnowledgePublication(BaseModel):
    id: UUID
    text: str
    timestamp: str
    author_id: int
    author_first_name: Optional[str] = ""
    author_last_name: Optional[str] = ""
    author_login: Optional[str] = ""
    published_channel_id: int
    published_message_id: int
    tags: Optional[list[str]] = []
