"""
Graph Retriever

Retrieves graph data from Neo4j.
"""

from graph.graph_query import GraphQuery
from utils.logger import get_logger

logger = get_logger(__name__)


class GraphRetriever:
    """
    Retrieves graph results.
    """

    def __init__(self):

        self.graph = GraphQuery()

    def retrieve(
        self,
        cypher: str,
        parameters: dict | None = None
    ) -> list:

        logger.info(
            "Retrieving graph results..."
        )

        return self.graph.execute(
            cypher,
            parameters or {}
        )