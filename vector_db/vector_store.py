"""
Vector Store

Stores and retrieves embeddings using ChromaDB.
"""

import chromadb

from utils.logger import get_logger

logger = get_logger(__name__)


class VectorStore:
    """
    ChromaDB Vector Store.
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="data/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="kaira"
        )

    def add_chunks(
        self,
        chunks: list[dict]
    ):

        logger.info(
            f"Adding {len(chunks)} chunks to ChromaDB..."
        )

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:

            ids.append(
                chunk["chunk_id"]
            )

            documents.append(
                chunk["content"]
            )

            embeddings.append(
                chunk["embedding"]
            )

            metadatas.append(
                {
                    "document_name": chunk["document_name"],
                    "chunk_number": chunk["chunk_number"],
                    "section": chunk["section"]
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

        logger.info(
            "Chunks stored successfully."
        )

    def search(
        self,
        embedding: list[float],
        top_k: int = 5
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )