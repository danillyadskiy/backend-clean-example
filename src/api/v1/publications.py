from http import HTTPStatus

from fastapi import APIRouter, Body, Depends

from api.v1.dependencies import get_create_publication_use_case, get_search_publications_use_case
from api.v1.mappers import PublicationCreationSummaryMapper, PublicationMapper
from api.v1.schema import PublicationCreatedSchema, PublicationCreationSummarySchema, PublicationSchema
from business import PublicationFilters
from business.use_case import CreatePublicationUseCase, SearchPublicationsUseCase

router = APIRouter()


@router.post(
    "/search/publications",
    status_code=HTTPStatus.OK,
    summary="Publications search",
    description="Search publication by text",
    response_model=list[PublicationSchema],
)
async def search_publications(
    filters: PublicationFilters = Body(default=None, embed=True),
    search_publications_use_case: SearchPublicationsUseCase = Depends(get_search_publications_use_case),
) -> list[PublicationSchema]:
    publications = await search_publications_use_case.search_publications(filters=filters)
    return PublicationMapper.list_from_business(publications)


@router.post(
    "/publications",
    status_code=HTTPStatus.CREATED,
    summary="Publication saving",
    description="Save publication with id and text",
    response_model=PublicationCreatedSchema,
)
async def post_publication(
    publication_to_post: PublicationCreationSummarySchema,
    create_publication_use_case: CreatePublicationUseCase = Depends(get_create_publication_use_case),
) -> PublicationCreatedSchema:
    publication_creation_summary = PublicationCreationSummaryMapper.to_business(publication_to_post)
    publication = await create_publication_use_case.create_publication(publication_creation_summary)
    return PublicationCreatedSchema(id=publication.id, timestamp=publication.timestamp)
