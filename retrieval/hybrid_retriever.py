"""
Hybrid Retriever

Combines graph retrieval and vector retrieval.
"""

from retrieval.graph_retriever import GraphRetriever
from retrieval.vector_retriever import VectorRetriever

from utils.logger import get_logger

logger = get_logger(__name__)


class HybridRetriever:
    """
    Performs hybrid retrieval.
    """

    def __init__(self):

        self.graph = GraphRetriever()
        self.vector = VectorRetriever()

    def retrieve(
        self,
        cypher: str,
        query: str,
        parameters: dict | None = None,
        top_k: int = 5
    ) -> dict:

        logger.info(
            "Performing hybrid retrieval..."
        )

        graph_results = self.graph.retrieve(
            cypher,
            parameters or {}
        )

        vector_results = self.vector.retrieve(
            query,
            top_k
        )

        return {
            "graph": graph_results,
            "vector": vector_results
        }