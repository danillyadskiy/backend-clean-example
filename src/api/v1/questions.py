from typing import List

from fastapi import APIRouter

from src.api.v1.fake.factory import get_fake_question, get_fake_questions
from src.api.v1.fake.schema import FakeQuestionSchema

router = APIRouter()


@router.get(
    "/question",
    response_model=FakeQuestionSchema,
    summary="Question",
    description="Get single question",
)
async def question() -> FakeQuestionSchema:  # pylint: disable=too-many-arguments
    return get_fake_question()


@router.get(
    "/questions",
    response_model=List[FakeQuestionSchema],
    summary="Question",
    description="Get list of questions",
)
async def questions_list() -> List[FakeQuestionSchema]:
    return get_fake_questions()
