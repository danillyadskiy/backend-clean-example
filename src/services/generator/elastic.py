from typing import Any, Dict

from functools import lru_cache


class EDSLGenerator:
    def generate_knowledge_publication_text_edsl(self, publication_text: str) -> Dict[str, Any]:
        # TODO: попробовать multi_match
        return {"query": {"multi_match": {"query": publication_text, "fields": ["text"], "type": "most_fields"}}}


@lru_cache()
def get_edsl_generator() -> EDSLGenerator:
    return EDSLGenerator()
