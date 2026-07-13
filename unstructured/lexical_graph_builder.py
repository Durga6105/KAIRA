"""
Lexical Graph Builder

Builds a lexical graph from document chunks.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class LexicalGraphBuilder:
    """
    Creates the lexical graph.
    """

    def build(
        self,
        metadata: dict,
        chunks: list[dict]
    ) -> dict:
        """
        Build lexical graph.

        Args:
            metadata: Document metadata.
            chunks: Document chunks.

        Returns:
            Lexical graph.
        """

        logger.info(
            "Building lexical graph..."
        )

        nodes = []

        relationships = []

        # -------------------------
        # Document Node
        # -------------------------

        document_node = {
            "type": "Document",
            "name": metadata["document_name"],
            "properties": metadata
        }

        nodes.append(document_node)

        # -------------------------
        # Chunk Nodes
        # -------------------------

        for chunk in chunks:

            chunk_node = {
                "type": "Chunk",
                "name": chunk["chunk_id"],
                "properties": chunk
            }

            nodes.append(chunk_node)

            relationships.append(
                {
                    "source": metadata["document_name"],
                    "target": chunk["chunk_id"],
                    "type": "HAS_CHUNK",
                    "properties": {
                        "chunk_number":
                        chunk["chunk_number"]
                    }
                }
            )

        logger.info(
            f"Lexical graph created ({len(nodes)} nodes, "
            f"{len(relationships)} relationships)."
        )

        return {
            "nodes": nodes,
            "relationships": relationships
        }