import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.ingestion_agent import (
    IngestionAgent
)


def main():

    agent = IngestionAgent()

    graph = agent.ingest(
        "uploads/unstructured/IRCTC_rules.pdf"
    )

    print()

    print("=" * 60)
    print("INGESTION SUCCESSFUL")
    print("=" * 60)

    print(
        "Nodes:",
        len(graph["nodes"])
    )

    print(
        "Relationships:",
        len(graph["relationships"])
    )

    print(
        "Chunks:",
        len(graph["chunks"])
    )


if __name__ == "__main__":
    main()