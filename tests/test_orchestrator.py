import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.orchestrator import Orchestrator


def main():

    orchestrator = Orchestrator()

    graph = orchestrator.ingest(
        "uploads/unstructured/onboarding_guide.pdf"
    )

    print()

    print("=" * 60)
    print("INGESTION SUCCESS")
    print("=" * 60)

    print(
        len(graph["nodes"])
    )

    print(
        len(graph["relationships"])
    )


if __name__ == "__main__":
    main()