"""
Graph Builder

Builds a final graph by combining
multiple graph components.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class GraphBuilder:
    """
    Combines multiple graphs.
    """

    def build(
        self,
        *graphs: dict
    ) -> dict:

        logger.info(
            "Building final graph..."
        )

        final_graph = {
            "nodes": [],
            "relationships": []
        }

        node_keys = set()
        relationship_keys = set()

        for graph in graphs:

            if not graph:
                continue

            for node in graph.get("nodes", []):

                key = (
                    node["type"],
                    node["name"]
                )

                if key in node_keys:
                    continue

                node_keys.add(key)

                final_graph["nodes"].append(node)

            for relationship in graph.get(
                "relationships",
                []
            ):

                key = (
                    relationship["source"],
                    relationship["target"],
                    relationship["type"]
                )

                if key in relationship_keys:
                    continue

                relationship_keys.add(key)

                final_graph["relationships"].append(
                    relationship
                )

        logger.info(
            f"Final graph: "
            f"{len(final_graph['nodes'])} nodes, "
            f"{len(final_graph['relationships'])} relationships."
        )

        return final_graph