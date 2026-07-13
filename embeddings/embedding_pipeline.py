"""
Embedding Pipeline

Generates embeddings for document chunks.
"""

from embeddings.embedding_generator import EmbeddingGenerator
from utils.logger import get_logger

logger = get_logger(__name__)


class EmbeddingPipeline:
    """
    Generates embeddings for chunks.
    """

    def __init__(self):

        self.generator = EmbeddingGenerator()

    def process(
        self,
        chunks: list[dict]
    ) -> list[dict]:

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks..."
        )

        embedded_chunks = []

        for chunk in chunks:

            embedding = self.generator.generate(
                chunk["content"]
            )

            chunk["embedding"] = embedding

            embedded_chunks.append(chunk)

        logger.info(
            "Embedding generation completed."
        )

        return embedded_chunks