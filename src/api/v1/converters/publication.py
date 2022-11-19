from api.v1.schema import PublicationSchema
from business import Author, Publication


class PublicationConverter:
    @staticmethod
    def from_business(publication: Publication) -> PublicationSchema:
        return PublicationSchema(
            id=publication.id,
            text=publication.text,
            tags=publication.tags,
            timestamp=publication.timestamp,
            author_id=publication.author.id,
            author_first_name=publication.author.first_name,
            author_last_name=publication.author.last_name,
            author_login=publication.author.login,
            published_channel_id=publication.published_channel_id,
            published_message_id=publication.published_message_id,
        )

    @staticmethod
    def to_business(publication_schema: PublicationSchema) -> Publication:
        return Publication(
            id=publication_schema.id,
            text=publication_schema.text,
            tags=publication_schema.tags,
            author=Author(
                id=publication_schema.author_id,
                first_name=publication_schema.author_first_name,
                last_name=publication_schema.author_last_name,
                login=publication_schema.author_login,
            ),
            timestamp=publication_schema.timestamp,
            published_channel_id=publication_schema.published_channel_id,
            published_message_id=publication_schema.published_message_id,
        )

    @staticmethod
    def list_from_business(publications: list[Publication]) -> list[PublicationSchema]:
        return [PublicationConverter.from_business(publication) for publication in publications]

    @staticmethod
    def list_to_business(publication_schemes: list[PublicationSchema]) -> list[Publication]:
        return [PublicationConverter.to_business(publication_schema) for publication_schema in publication_schemes]
