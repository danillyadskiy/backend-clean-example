import os
import sys

import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from storage.instances.elastic import storage
from elasticsearch import Elasticsearch

from core.settings import Settings
from services.loader.elastic import ElasticSearchLoader
from storage.instances.elastic.settings import KNOWLEDGE_INDEX_NAME, KNOWLEDGE_INDEX_SETTINGS

sys.path.append(os.getcwd())
settings = Settings()

from api.v1 import publications  # noqa

app = FastAPI(
    title="search-api",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup() -> None:
    storage.elastic_storage = AsyncElasticsearch(hosts=[settings.elastic])


@app.on_event("shutdown")
async def shutdown() -> None:
    ...


app.include_router(publications.router, prefix="/api/v1", tags=["publications"])

def create_index_if_not_exist():
    es_client = Elasticsearch(hosts=[settings.elastic])

    if not es_client.indices.exists(KNOWLEDGE_INDEX_NAME):
        ElasticSearchLoader(es_client).create_mapping(index_name=KNOWLEDGE_INDEX_NAME, body=KNOWLEDGE_INDEX_SETTINGS)


if __name__ == "__main__":
    create_index_if_not_exist()
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # nosec
        port=8000,
    )
