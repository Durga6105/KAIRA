"""
Graph Query

Executes Cypher queries against Neo4j.
"""

from graph.neo4j_client import Neo4jClient
from utils.logger import get_logger

logger = get_logger(__name__)


class GraphQuery:
    """
    Executes graph queries.
    """

    def __init__(self):

        self.client = Neo4jClient()

    def execute(
        self,
        query: str,
        parameters: dict | None = None
    ) -> list:

        logger.info(
            "Executing Cypher query..."
        )

        return self.client.execute(
            query,
            parameters or {}
        )

    def close(self):

        self.client.close()