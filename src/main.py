import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import publications
from core.config import SETTINGS
from core.elastic_config import KNOWLEDGE_INDEX_NAME, KNOWLEDGE_INDEX_SETTINGS, es_client
from gateways.elastic.services import SearchLoader

app = FastAPI(
    title="search-api",
    version=SETTINGS.version,
    docs_url="/api/openapi" if SETTINGS.debug else None,
    openapi_url="/api/openapi.json" if SETTINGS.debug else None,
    default_response_class=ORJSONResponse,
)

app.include_router(publications.router, prefix="/api/v1", tags=["publications"])


@app.on_event("startup")
async def app_startup() -> None:
    if not await es_client.indices.exists(KNOWLEDGE_INDEX_NAME):
        await SearchLoader(es_client).create_mapping(index_name=KNOWLEDGE_INDEX_NAME, body=KNOWLEDGE_INDEX_SETTINGS)


@app.on_event("shutdown")
async def app_shutdown() -> None:
    await es_client.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host=SETTINGS.hostname, port=SETTINGS.port)
