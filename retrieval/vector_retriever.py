"""
Vector Retriever

Retrieves relevant chunks from ChromaDB.
"""

from embeddings.embedding_generator import EmbeddingGenerator
from vector_db.vector_store import VectorStore
from utils.logger import get_logger

logger = get_logger(__name__)


class VectorRetriever:
    """
    Retrieves relevant chunks using vector similarity.
    """

    def __init__(self):

        self.embedder = EmbeddingGenerator()
        self.store = VectorStore()

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ) -> list:

        logger.info(
            "Performing vector search..."
        )

        embedding = self.embedder.generate(
            query
        )

        results = self.store.search(
            embedding,
            top_k
        )

        return results