import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from unstructured.unstructured_pipeline import (
    UnstructuredPipeline
)


def main():

    pipeline = UnstructuredPipeline()

    graph = pipeline.process(
        "uploads/unstructured/budget_2026.pdf"
    )

    print("\nGRAPH SUMMARY")
    print("=" * 60)

    print(
        f"Document      : {graph['metadata']['document_name']}"
    )

    print(
        f"Nodes         : {len(graph['nodes'])}"
    )

    print(
        f"Relationships : {len(graph['relationships'])}"
    )


if __name__ == "__main__":
    main()