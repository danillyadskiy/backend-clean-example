from pydantic import BaseModel

from business.author import Author


class PublicationCreationSummary(BaseModel):
    text: str
    tags: list[str]
    author: Author
    published_channel_id: int
    published_message_id: int
