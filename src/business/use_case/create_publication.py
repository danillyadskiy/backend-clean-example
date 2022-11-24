from business import Publication, PublicationCreationSummary
from business.interfaces import IPublicationSaver


class CreatePublicationUseCase:
    def __init__(self, publication_saver: IPublicationSaver):
        self.__publication_saver = publication_saver

    async def create_publication(self, publication_creation_summary: PublicationCreationSummary) -> Publication:
        publication = Publication.parse_obj(publication_creation_summary)
        await self.__publication_saver.save(publication)
        return publication
