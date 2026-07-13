"""
Schema Loader

Loads the current Neo4j graph schema.
"""

from graph.neo4j_client import Neo4jClient
from utils.logger import get_logger

logger = get_logger(__name__)


class SchemaLoader:
    """
    Loads Neo4j graph schema.
    """

    def __init__(self):

        self.client = Neo4jClient()

    def load(self) -> str:
        """
        Returns the graph schema as text.
        """

        logger.info(
            "Loading graph schema..."
        )

        with self.client.driver.session() as session:

            # ----------------------------------
            # Labels
            # ----------------------------------

            labels = session.run(
                "CALL db.labels()"
            )

            label_list = [
                record["label"]
                for record in labels
            ]

            # ----------------------------------
            # Relationship Types
            # ----------------------------------

            relationships = session.run(
                "CALL db.relationshipTypes()"
            )

            relationship_list = [
                record["relationshipType"]
                for record in relationships
            ]

            # ----------------------------------
            # Property Keys
            # ----------------------------------

            properties = session.run(
                "CALL db.propertyKeys()"
            )

            property_list = [
                record["propertyKey"]
                for record in properties
            ]

            # ----------------------------------
            # Example Graph Patterns
            # ----------------------------------

            patterns = session.run(
                """
                MATCH (a)-[r]->(b)

                RETURN DISTINCT
                    labels(a) AS source,
                    type(r) AS relationship,
                    labels(b) AS target

                LIMIT 20
                """
            )

            pattern_list = []

            for record in patterns:

                source = ":".join(
                    record["source"]
                )

                target = ":".join(
                    record["target"]
                )

                relationship = record[
                    "relationship"
                ]

                pattern_list.append(
                    f"({source})-[:{relationship}]->({target})"
                )

        schema = f"""
====================================================
NODE LABELS
====================================================

{chr(10).join(label_list)}

====================================================
RELATIONSHIP TYPES
====================================================

{chr(10).join(relationship_list)}

====================================================
PROPERTY KEYS
====================================================

{chr(10).join(property_list)}

====================================================
EXAMPLE GRAPH PATTERNS
====================================================

{chr(10).join(pattern_list)}
"""

        logger.info(
            "Schema loaded successfully."
        )

        return schema