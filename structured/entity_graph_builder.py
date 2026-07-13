"""
Structured Entity Graph Builder

Builds an in-memory graph representation from
metadata, schema, entities and relationships.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class EntityGraphBuilder:
    """
    Builds a graph representation of structured data.
    """

    def build(
        self,
        metadata: dict,
        schema: dict,
        entities: list,
        relationships: list
    ) -> dict:
        """
        Build graph object.
        """

        logger.info("Building entity graph...")

        graph = {

            "metadata": metadata,

            "schema": schema,

            "nodes": entities,

            "relationships": relationships

        }

        logger.info(
            f"Graph built successfully "
            f"({len(entities)} nodes, "
            f"{len(relationships)} relationships)"
        )

        return graph