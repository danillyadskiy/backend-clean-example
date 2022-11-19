from api.v1.schema import PublicationCreationSummarySchema
from business import Author, PublicationCreationSummary


class PublicationCreationSummaryConverter:
    @staticmethod
    def from_business(publication_creation_summary: PublicationCreationSummary) -> PublicationCreationSummarySchema:
        return PublicationCreationSummarySchema(
            text=publication_creation_summary.text,
            tags=publication_creation_summary.tags,
            author_id=publication_creation_summary.author.id,
            author_first_name=publication_creation_summary.author.first_name,
            author_last_name=publication_creation_summary.author.last_name,
            author_login=publication_creation_summary.author.login,
            published_channel_id=publication_creation_summary.published_channel_id,
            published_message_id=publication_creation_summary.published_message_id,
        )

    @staticmethod
    def to_business(
        publication_creation_summary_schema: PublicationCreationSummarySchema,
    ) -> PublicationCreationSummary:
        return PublicationCreationSummary(
            text=publication_creation_summary_schema.text,
            tags=publication_creation_summary_schema.tags,
            author=Author(
                id=publication_creation_summary_schema.author_id,
                first_name=publication_creation_summary_schema.author_first_name,
                last_name=publication_creation_summary_schema.author_last_name,
                login=publication_creation_summary_schema.author_login,
            ),
            published_channel_id=publication_creation_summary_schema.published_channel_id,
            published_message_id=publication_creation_summary_schema.published_message_id,
        )

    @staticmethod
    def list_from_business(
        publication_creation_summaries: list[PublicationCreationSummary],
    ) -> list[PublicationCreationSummarySchema]:
        return [
            PublicationCreationSummaryConverter.from_business(publication_creation_summary)
            for publication_creation_summary in publication_creation_summaries
        ]

    @staticmethod
    def list_to_business(
        publication_creation_summary_schemes: list[PublicationCreationSummarySchema],
    ) -> list[PublicationCreationSummary]:
        return [
            PublicationCreationSummaryConverter.to_business(publication_creation_summary_schema)
            for publication_creation_summary_schema in publication_creation_summary_schemes
        ]
