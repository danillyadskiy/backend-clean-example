from typing import List

from datetime import datetime
from http import HTTPStatus
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException

from api.v1.schema.question import PostQuestionSchema
from services.generator.elastic import EDSLGenerator, get_edsl_generator
from services.loader.service import QuestionsLoaderService, get_questions_loader_service
from services.search.service import Question, QuestionsSearchService, get_questions_search_service
from src.api.v1.fake.factory import get_fake_question
from src.api.v1.fake.schema import FakeQuestionSchema

router = APIRouter()


# TODO: вынести отсюда эту функцию
def posted_question_schema_to_question_model(posted_question: PostQuestionSchema) -> Question:
    return Question(text=posted_question.text, id=posted_question.id, timestamp=datetime.now().timestamp())


@router.get(
    "/question",
    response_model=FakeQuestionSchema,
    summary="Question",
    description="Get single question",
)
async def get_question() -> FakeQuestionSchema:  # pylint: disable=too-many-arguments
    return get_fake_question()


@router.post(
    "/search/questions",
    status_code=HTTPStatus.CREATED,
    summary="Questions search",
    description="Search question by text",
)
async def get_questions_list(
    question_text: str,
    edsl_generator: EDSLGenerator = Depends(get_edsl_generator),
    search_service: QuestionsSearchService = Depends(get_questions_search_service),
) -> List[Question]:
    edsl = edsl_generator.generate_question_text_edsl(question_text)
    questions = await search_service.search_question(edsl)
    return questions


# TODO: добавить возвращаемый тип
@router.post("/questions",
             status_code=HTTPStatus.CREATED,
             summary="Question saving",
             description="Save question with id and text",
             )
async def post_question(  # type:ignore
    posted_question: PostQuestionSchema, loader_service: QuestionsLoaderService = Depends(get_questions_loader_service)
):
    question_detail = posted_question_schema_to_question_model(posted_question)
    is_uploaded = loader_service.upload_question(question_detail)

    if is_uploaded:
        return question_detail
    else:
        # TODO: нужно проработать варианты ошибок
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
