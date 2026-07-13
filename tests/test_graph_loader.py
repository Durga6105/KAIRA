import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from structured.structured_pipeline import StructuredPipeline
from graph.graph_loader import GraphLoader
def main():

    pipeline = StructuredPipeline()

    graph = pipeline.process(
        "uploads/structured/employee.json"
    )

    loader = GraphLoader()

    loader.load(graph)

    loader.close()

    print()

    print("Graph loaded successfully.")


if __name__ == "__main__":
    main()