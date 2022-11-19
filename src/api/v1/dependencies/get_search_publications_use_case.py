from business.use_case import SearchPublicationsUseCase
from core.elastic_config import es_client
from gateways.elastic import PublicationGateway


def get_search_publications_use_case() -> SearchPublicationsUseCase:
    return SearchPublicationsUseCase(PublicationGateway(search=es_client))
