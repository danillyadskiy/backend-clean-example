from typing import Any, Optional

from business import PublicationFilters


class EDSLGenerator:
    @staticmethod
    def generate_publication_query_edsl(edsl_filters: Optional[list[dict[str, Any]]] = None) -> dict[str, Any]:
        return {"query": {"bool": {"must": edsl_filters}}} if edsl_filters else {}

    @staticmethod
    def generate_publication_filters_edsl(filters: PublicationFilters) -> list[dict[str, Any]]:
        edsl_filters = []

        if filters.text:
            edsl_filters.append(EDSLGenerator.generate_publication_text_filter_edsl(filters.text))

        if filters.tags:
            edsl_filters.append(EDSLGenerator.generate_publication_tags_filter_edsl(filters.tags))

        return edsl_filters

    @staticmethod
    def generate_publication_text_filter_edsl(text: str) -> dict[str, Any]:
        return {"match": {"text": {"query": text, "fuzziness": "auto"}}}

    @staticmethod
    def generate_publication_tags_filter_edsl(tags: list[str]) -> dict[str, Any]:
        return {"terms": {"tags.keyword": tags}}
