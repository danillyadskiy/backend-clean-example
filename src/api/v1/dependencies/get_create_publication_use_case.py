from business.use_case import CreatePublicationUseCase
from core.elastic_config import es_client
from gateways.elastic import PublicationGateway


def get_create_publication_use_case() -> CreatePublicationUseCase:
    return CreatePublicationUseCase(PublicationGateway(search=es_client))
