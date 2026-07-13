import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from retrieval.hybrid_retriever import (
    HybridRetriever
)


def main():

    retriever = HybridRetriever()

    results = retriever.retrieve(
        cypher="""
        MATCH (p:Entity)-[:HAS_EMAIL]->(e:Entity)
        WHERE p.name="Jane Doe"
        RETURN p.name AS person,
               e.name AS email
        """,
        query="What is Jane Doe's email?"
    )

    print("\nGRAPH")
    print("=" * 60)
    print(results["graph"])

    print("\nVECTOR")
    print("=" * 60)
    print(results["vector"])


if __name__ == "__main__":
    main()