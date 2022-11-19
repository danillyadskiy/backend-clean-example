from business import Publication, PublicationCreationSummary
from business.interfaces import IPublicationGateway


class CreatePublicationUseCase:
    def __init__(self, publication_gateway: IPublicationGateway):
        self.__publication_gateway = publication_gateway

    async def create_publication(self, publication_creation_summary: PublicationCreationSummary) -> Publication:
        publication = Publication.parse_obj(publication_creation_summary)
        await self.__publication_gateway.save(publication)
        return publication
