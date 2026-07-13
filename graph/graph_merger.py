"""
Graph Merger

Merges multiple knowledge graphs into one.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class GraphMerger:
    """
    Merges multiple graphs.
    """

    def merge(
        self,
        graphs: list[dict]
    ) -> dict:

        logger.info(
            f"Merging {len(graphs)} graphs..."
        )

        merged = {
            "nodes": [],
            "relationships": []
        }

        node_keys = set()
        relationship_keys = set()

        for graph in graphs:

            if not graph:
                continue

            for node in graph.get(
                "nodes",
                []
            ):

                key = (
                    node["type"],
                    node["name"].lower()
                )

                if key in node_keys:
                    continue

                node_keys.add(key)

                merged["nodes"].append(
                    node
                )

            for relationship in graph.get(
                "relationships",
                []
            ):

                key = (
                    relationship["source"].lower(),
                    relationship["target"].lower(),
                    relationship["type"].upper()
                )

                if key in relationship_keys:
                    continue

                relationship_keys.add(key)

                merged["relationships"].append(
                    relationship
                )

        logger.info(
            f"Merged graph contains "
            f"{len(merged['nodes'])} nodes and "
            f"{len(merged['relationships'])} relationships."
        )

        return merged