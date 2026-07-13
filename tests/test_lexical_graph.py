import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from unstructured.text_extractor import TextExtractor
from unstructured.metadata_extractor import MetadataExtractor
from unstructured.chunker import Chunker
from unstructured.lexical_graph_builder import LexicalGraphBuilder


def main():

    file_path = "uploads/unstructured/budget_2026.pdf"

    text = TextExtractor().extract(file_path)

    metadata = MetadataExtractor().extract(file_path)

    chunks = Chunker().chunk(text)

    graph = LexicalGraphBuilder().build(
        metadata,
        chunks
    )

    print("\nLEXICAL GRAPH")
    print("=" * 60)

    print(f"Nodes : {len(graph['nodes'])}")
    print(f"Relationships : {len(graph['relationships'])}")

    print("\nFirst Relationship")
    print("=" * 60)
    print(graph["relationships"][0])


if __name__ == "__main__":
    main()