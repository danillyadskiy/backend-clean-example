from typing import Optional

from pydantic import BaseModel


class PublicationCreationSummarySchema(BaseModel):
    text: str
    tags: list[str]
    author_id: int
    author_first_name: Optional[str]
    author_last_name: Optional[str]
    author_login: str
    published_channel_id: int
    published_message_id: int
