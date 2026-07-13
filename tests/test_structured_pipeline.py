import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from structured.structured_pipeline import StructuredPipeline


def main():

    pipeline = StructuredPipeline()

    graph = pipeline.process(
        "uploads/structured/document.xlsx"
    )

    print("\nGRAPH SUMMARY")
    print("=" * 60)
    print(f"Document      : {graph['metadata']['document_name']}")
    print(f"Nodes         : {len(graph['nodes'])}")
    print(f"Relationships : {len(graph['relationships'])}")

    print("\nRelationships")
    print("=" * 60)

    for relationship in graph["relationships"]:
        print(relationship)

    print("\nMetadata")
    print("=" * 60)
    print(graph["metadata"])

    print("\nSchema")
    print("=" * 60)
    print(graph["schema"])


if __name__ == "__main__":
    main()