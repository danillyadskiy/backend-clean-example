from typing import Any, Dict

from functools import lru_cache


class EDSLGenerator:
    def generate_knowledge_publication_text_edsl(self, publication_text: str) -> Dict[str, Any]:
        return {"query": {"match": {"text": {"query": publication_text, "fuzziness": "auto"}}}}


@lru_cache()
def get_edsl_generator() -> EDSLGenerator:
    return EDSLGenerator()
