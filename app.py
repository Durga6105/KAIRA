"""
KAIRA

Application entry point.
"""

from fastapi import FastAPI

from api.health_api import router as health_router
from api.ingestion_api import router as ingestion_router
from api.query_api import router as query_router


app = FastAPI(

    title="KAIRA",

    description="Enterprise Knowledge Graph & Hybrid GraphRAG Platform",

    version="1.0.0"

)


app.include_router(
    health_router
)

app.include_router(
    ingestion_router
)

app.include_router(
    query_router
)


@app.get(
    "/",
    summary="KAIRA Home"
)
def root():

    return {

        "application": "KAIRA",

        "version": "1.0.0",

        "status": "Running"

    }