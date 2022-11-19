from typing import Any


class EDSLGenerator:
    @staticmethod
    def generate_publication_text_edsl(publication_text: str) -> dict[str, Any]:
        return {"query": {"match": {"text": {"query": publication_text, "fuzziness": "auto"}}}}
