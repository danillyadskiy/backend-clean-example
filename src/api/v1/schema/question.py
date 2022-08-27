from uuid import UUID

from pydantic import BaseModel


class QuestionSchema(BaseModel):
    id: UUID
    body: str
