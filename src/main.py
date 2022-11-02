import os
import sys

import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.settings import Settings
from storage.instances.elastic import storage

sys.path.append(os.getcwd())
settings = Settings()

from src.api.v1 import publications  # noqa

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

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # nosec
        port=8000,
    )
