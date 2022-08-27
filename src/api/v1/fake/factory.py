from typing import List

import random

import lorem
from pydantic_factories import ModelFactory

from src.api.v1.fake.schema import FakeQuestionSchema


class FakeQuestionFactory(ModelFactory):
    __model__ = FakeQuestionSchema


def get_fake_question() -> FakeQuestionSchema:
    return FakeQuestionFactory.build(body=lorem.paragraph())


def get_fake_questions() -> List[FakeQuestionSchema]:
    return list(
        map(
            lambda question: FakeQuestionSchema(id=question.id, body=lorem.paragraph()),
            FakeQuestionFactory.batch(random.randint(0, 10)),  # nosec
        )
    )
