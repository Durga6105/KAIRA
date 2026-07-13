from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from agents.ingestion_agent import IngestionAgent


router = APIRouter(
    prefix="/ingestion",
    tags=["Ingestion"]
)


class IngestionRequest(BaseModel):
    file_path: str


agent = IngestionAgent()


@router.post("/")
def ingest(request: IngestionRequest):

    try:

        graph = agent.ingest(
            request.file_path
        )

        return {
            "message": "Ingestion completed successfully.",
            "nodes": len(graph["nodes"]),
            "relationships": len(graph["relationships"])
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )