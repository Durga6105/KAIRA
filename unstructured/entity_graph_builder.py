"""
Unstructured Entity Graph Builder
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class EntityGraphBuilder:
    """
    Builds the final knowledge graph.
    """

    def build(
        self,
        metadata: dict,
        lexical_graph: dict,
        entities: list,
        relationships: list
    ) -> dict:
        """
        Build the final entity graph.

        Args:
            metadata: Document metadata.
            lexical_graph: Lexical graph.
            entities: Normalized & deduplicated entities.
            relationships: Normalized & deduplicated relationships.

        Returns:
            Final knowledge graph.
        """

        logger.info(
            "Building entity graph..."
        )

        nodes = lexical_graph["nodes"].copy()

        edges = lexical_graph["relationships"].copy()

        existing = {
            (
                node["type"].lower(),
                node["name"].lower()
            )
            for node in nodes
        }

        # -------------------------
        # Add Entity Nodes
        # -------------------------

        for entity in entities:

            key = (
                entity["type"].lower(),
                entity["name"].lower()
            )

            if key in existing:
                continue

            existing.add(key)

            nodes.append(
                {
                    "type": entity["type"],
                    "name": entity["name"],
                    "properties": entity.get(
                        "properties",
                        {}
                    )
                }
            )

        # -------------------------
        # Add Entity Relationships
        # -------------------------

        edges.extend(
            relationships
        )

        logger.info(
            f"Graph built successfully "
            f"({len(nodes)} nodes, "
            f"{len(edges)} relationships)"
        )

        return {
            "metadata": metadata,
            "nodes": nodes,
            "relationships": edges
        }