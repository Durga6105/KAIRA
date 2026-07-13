"""
Query API
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from agents.retrieval_agent import RetrievalAgent

router = APIRouter(
    prefix="/query",
    tags=["Query"]
)


class QueryRequest(BaseModel):

    question: str


agent = RetrievalAgent()


@router.post(
    "/",
    summary="Query the Enterprise Knowledge Graph"
)
def query(
    request: QueryRequest
):

    try:

        answer = agent.query(
            request.question
        )

        return {

            "answer": answer

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )