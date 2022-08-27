import os
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

sys.path.append(os.getcwd())

from src.api.v1 import questions  # noqa

app = FastAPI(
    title="mock-api",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup() -> None:
    ...


@app.on_event("shutdown")
async def shutdown() -> None:
    ...


app.include_router(questions.router, prefix="/api/v1", tags=["questions"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # nosec
        port=8000,
    )
