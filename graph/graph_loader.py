"""
Graph Loader

Loads graph data into Neo4j.
"""

import re

from graph.neo4j_client import Neo4jClient
from utils.logger import get_logger

logger = get_logger(__name__)


class GraphLoader:
    """
    Loads nodes and relationships into Neo4j.
    """

    def __init__(self):

        self.client = Neo4jClient()

    def load(self, graph: dict):
        """
        Load graph into Neo4j.
        """

        logger.info("Loading graph into Neo4j...")

        self._create_nodes(graph["nodes"])

        self._create_relationships(graph["relationships"])

        logger.info("Graph loaded successfully.")

    def _sanitize(self, value: str) -> str:
        """
        Convert labels/relationship types into valid Cypher identifiers.
        """

        return re.sub(r"[^A-Za-z0-9_]", "_", value)

    def _create_nodes(
        self,
        nodes: list
    ):

        for node in nodes:

            label = self._sanitize(
                node["type"]
            )

            query = f"""
            MERGE (n:Entity:{label} {{name:$name}})

            SET
                n.type = $type

            SET
                n += $properties
            """

            self.client.execute(
                query,
                {
                    "name": node["name"],
                    "type": node["type"],
                    "properties": node.get(
                        "properties",
                        {}
                    )
                }
            )

    def _create_relationships(
        self,
        relationships: list
    ):

        for relationship in relationships:

            relation = self._sanitize(
                relationship["type"]
            )

            query = f"""
            MATCH (a {{name:$source}})
            MATCH (b {{name:$target}})

            MERGE (a)-[r:{relation}]->(b)

            SET
                r += $properties
            """

            self.client.execute(
                query,
                {
                    "source": relationship["source"],
                    "target": relationship["target"],
                    "properties": relationship.get(
                        "properties",
                        {}
                    )
                }
            )

    def close(self):

        self.client.close()