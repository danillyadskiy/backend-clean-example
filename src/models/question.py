from uuid import UUID

from pydantic import BaseModel


class QuestionModel(BaseModel):
    id: UUID
    body: str
