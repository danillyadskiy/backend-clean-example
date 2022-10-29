from typing import List, Optional

from datetime import datetime
from http import HTTPStatus
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException

from api.v1.schema.publication import PostPublicationSchema, PublicationSchema
from models.knowledge_publication import KnowledgePublication
from services.generator.elastic import EDSLGenerator, get_edsl_generator
from services.loader.service import KnowledgePublicationsLoaderService, get_knowledge_publications_loader_service
from services.search.service import KnowledgePublicationsSearchService, get_knowledge_publications_search_service

router = APIRouter()


# TODO: вынести отсюда эту функцию
def posted_publication_to_knowledge_publication(posted_publication: PostPublicationSchema) -> KnowledgePublication:
    return KnowledgePublication(**posted_publication.dict(), id=str(uuid4()), timestamp=datetime.now().timestamp())


def knowledge_publication_to_publication_schema(publication: KnowledgePublication) -> PublicationSchema:
    return PublicationSchema(id=publication.id, text=publication.text)


@router.post(
    "/search/publications",
    status_code=HTTPStatus.CREATED,
    summary="Publications search",
    description="Search publication by text",
    response_model=List[KnowledgePublication],
)
async def search_publications(
    publication_text: str,
    edsl_generator: EDSLGenerator = Depends(get_edsl_generator),
    search_service: KnowledgePublicationsSearchService = Depends(get_knowledge_publications_search_service),
    # TODO: тут по идее async возвращаемый тип
) -> List[KnowledgePublication]:
    edsl = edsl_generator.generate_knowledge_publication_text_edsl(publication_text)
    return await search_service.search_publications(edsl)


# TODO: Нужно заменить KnowledgePublication на PublicationSchema
@router.post(
    "/publications",
    status_code=HTTPStatus.CREATED,
    summary="Publication saving",
    description="Save publication with id and text",
    response_model=PublicationSchema,
)
async def post_publication(
    publication_to_post: PostPublicationSchema,
    loader_service: KnowledgePublicationsLoaderService = Depends(get_knowledge_publications_loader_service),
) -> Optional[PublicationSchema]:
    knowledge_publication = posted_publication_to_knowledge_publication(publication_to_post)
    is_uploaded = loader_service.upload_knowledge_publication(knowledge_publication)

    if is_uploaded:
        return knowledge_publication_to_publication_schema(knowledge_publication)
    else:
        # TODO: нужно проработать варианты ошибок
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
