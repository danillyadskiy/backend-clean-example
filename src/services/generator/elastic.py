from typing import Any, Dict

from functools import lru_cache


class EDSLGenerator:
    def generate_question_text_edsl(self, question_text: str) -> Dict[str, Any]:
        # TODO: попробовать multi_match
        return {"query": {"multi_match": {"query": question_text, "fields": ["text"], "type": "most_fields"}}}


@lru_cache()
def get_edsl_generator() -> EDSLGenerator:
    return EDSLGenerator()
