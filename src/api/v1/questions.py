from typing import List

from datetime import datetime
from http import HTTPStatus
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException

from api.v1.schema.question import PostQuestionSchema
from services.loader.service import QuestionsLoaderService, get_questions_loader_service
from services.search.service import Question
from src.api.v1.fake.factory import get_fake_question, get_fake_questions
from src.api.v1.fake.schema import FakeQuestionSchema

router = APIRouter()


# TODO: вынести отсюда эту функцию
def posted_question_schema_to_question_model(posted_question: PostQuestionSchema) -> Question:
    return Question(text=posted_question.text, id=uuid4(), timestamp=datetime.now().timestamp())


@router.get(
    "/question",
    response_model=FakeQuestionSchema,
    summary="Question",
    description="Get single question",
)
async def get_question() -> FakeQuestionSchema:  # pylint: disable=too-many-arguments
    return get_fake_question()


@router.get(
    "/questions",
    response_model=List[FakeQuestionSchema],
    summary="Question",
    description="Get list of questions",
)
async def get_questions_list() -> List[FakeQuestionSchema]:
    return get_fake_questions()


# TODO: добавить возвращаемый тип
@router.post("/questions", status_code=HTTPStatus.CREATED)
async def post_question(  # type:ignore
    posted_question: PostQuestionSchema, loader_service: QuestionsLoaderService = Depends(get_questions_loader_service)
):
    is_uploaded = loader_service.upload_question(posted_question_schema_to_question_model(posted_question))

    if is_uploaded:
        return {}
    else:
        # TODO: нужно проработать варианты ошибок
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
