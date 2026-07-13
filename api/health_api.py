"""
Health API
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get(
    "/",
    summary="Health Check"
)
def health():

    return {

        "status": "healthy",

        "application": "KAIRA",

        "version": "1.0.0"

    }