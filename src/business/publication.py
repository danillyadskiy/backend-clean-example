from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from business.author import Author


class Publication(BaseModel):
    id: UUID = Field(default_factory=uuid4, allow_mutation=False)
    text: str
    tags: list[str]
    author: Author
    timestamp: float = Field(datetime.now().timestamp(), allow_mutation=False)
    published_channel_id: int
    published_message_id: int

    class Config:
        validate_assignment = True
