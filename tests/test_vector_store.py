import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from unstructured.text_extractor import TextExtractor
from unstructured.chunker import Chunker

from embeddings.embedding_pipeline import (
    EmbeddingPipeline
)

from vector_db.vector_store import (
    VectorStore
)


def main():

    text = TextExtractor().extract(
        "uploads/unstructured/budget_2026.pdf"
    )

    chunks = Chunker().chunk(text)

    chunks = EmbeddingPipeline().process(
        chunks
    )

    store = VectorStore()

    store.add_chunks(
        chunks
    )

    print("\nStored Successfully")


if __name__ == "__main__":
    main()