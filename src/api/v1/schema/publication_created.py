from uuid import UUID

from pydantic import BaseModel


class PublicationCreatedSchema(BaseModel):
    id: UUID
    text: str