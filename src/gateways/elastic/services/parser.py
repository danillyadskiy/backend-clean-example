from typing import Any, Type

from pydantic import parse_obj_as
from pydantic.main import BaseModel


class EDSLParser:
    @staticmethod
    def hits_to_model_list(list_model: Type[list[BaseModel]], es_docs: dict[str, Any]) -> list[BaseModel]:
        values_dict = [item["_source"] for item in es_docs["hits"]["hits"]]
        objs = parse_obj_as(list_model, values_dict)
        return objs
