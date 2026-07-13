"""
KAIRA Orchestrator

Coordinates all KAIRA workflows.
"""

from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent

from utils.logger import get_logger

logger = get_logger(__name__)


class Orchestrator:
    """
    Master orchestrator.
    """

    def __init__(self):

        self.ingestion_agent = IngestionAgent()

        self.retrieval_agent = RetrievalAgent()

    def ingest(
        self,
        file_path: str
    ) -> dict:
        """
        Ingest a document.
        """

        logger.info(
            "Executing ingestion workflow..."
        )

        return self.ingestion_agent.ingest(
            file_path
        )

    def query(
        self,
        question: str
    ) -> str:
        """
        Execute retrieval workflow.
        """

        logger.info(
            "Executing retrieval workflow..."
        )

        return self.retrieval_agent.query(
            question
        )