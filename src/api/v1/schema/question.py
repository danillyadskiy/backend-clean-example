from uuid import UUID

from pydantic import BaseModel


class QuestionSchema(BaseModel):
    id: UUID
    text: str


class PostQuestionSchema(BaseModel):
    # TODO: схему можно дополнять, добавляя поля из модели elastic
    text: str
    id: UUID
