from pydantic import BaseModel


class PublicationCreationSummarySchema(BaseModel):
    text: str
    tags: list[str]
    author_id: int
    author_first_name: str
    author_last_name: str
    author_login: str
    published_channel_id: int
    published_message_id: int
