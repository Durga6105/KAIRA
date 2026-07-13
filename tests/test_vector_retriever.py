import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from retrieval.vector_retriever import (
    VectorRetriever
)


def main():

    retriever = VectorRetriever()

    results = retriever.retrieve(
        "Who approves budget above 10 lakhs?"
    )

    print(results)


if __name__ == "__main__":
    main()