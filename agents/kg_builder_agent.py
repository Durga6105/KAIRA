"""
Knowledge Graph Builder Agent

Builds the complete knowledge graph and indexes it.
"""

from structured.structured_pipeline import StructuredPipeline
from unstructured.unstructured_pipeline import UnstructuredPipeline

from graph.graph_loader import GraphLoader

from embeddings.embedding_pipeline import EmbeddingPipeline
from vector_db.vector_store import VectorStore

from utils.logger import get_logger

logger = get_logger(__name__)


class KGBuilderAgent:
    """
    Builds and indexes a knowledge graph.
    """

    def __init__(self):

        self.structured = StructuredPipeline()

        self.unstructured = UnstructuredPipeline()

        self.graph_loader = GraphLoader()

        self.embedding_pipeline = EmbeddingPipeline()

        self.vector_store = VectorStore()

    def build(
        self,
        file_path: str,
        file_type: str
    ) -> dict:
        """
        Build and index a knowledge graph.
        """

        logger.info(
            "Building Knowledge Graph..."
        )

        # -----------------------------
        # Build graph
        # -----------------------------

        if file_type == "structured":

            graph = self.structured.process(
                file_path
            )

        else:

            graph = self.unstructured.process(
                file_path
            )

        # -----------------------------
        # Neo4j
        # -----------------------------

        self.graph_loader.load(
            graph
        )

        # -----------------------------
        # ChromaDB
        # -----------------------------

        chunks = graph.get(
            "chunks",
            []
        )

        if chunks:

            embedded_chunks = (
                self.embedding_pipeline.process(
                    chunks
                )
            )

            self.vector_store.add_chunks(
                embedded_chunks
            )

        logger.info(
            "Knowledge Graph built successfully."
        )

        return graph