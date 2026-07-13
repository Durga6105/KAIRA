"""
Neo4j Client

Handles Neo4j database connection.
"""

from neo4j import GraphDatabase

from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class Neo4jClient:
    """
    Neo4j database client.
    """

    def __init__(self):

        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(
                settings.NEO4J_USERNAME,
                settings.NEO4J_PASSWORD
            )
        )

        logger.info(
            "Neo4j client initialized successfully."
        )

    def execute(
        self,
        query: str,
        parameters: dict | None = None
    ):
        """
        Execute a Cypher query.
        """

        with self.driver.session() as session:

            result = session.run(
                query,
                parameters or {}
            )

            return list(result)

    def close(self):

        self.driver.close()

    def health_check(self) -> bool:
        """
        Check Neo4j connectivity.
        """

        try:

            self.execute(
                "RETURN 'OK' AS status"
            )

            return True

        except Exception as e:

            logger.error(e)

            return False