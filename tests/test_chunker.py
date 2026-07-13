import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from unstructured.text_extractor import TextExtractor
from unstructured.chunker import Chunker


def main():

    extractor = TextExtractor()

    document = extractor.extract(
        "uploads/unstructured/budget_2026.pdf"
    )

    chunker = Chunker()

    chunks = chunker.chunk(document)

    print("\nTOTAL CHUNKS")
    print("=" * 60)
    for chunk in chunks:
        print(chunk["chunk_number"])
        print(chunk["section"])
        print(chunk["word_count"])
        print("-" * 60)
        print(chunk["content"])
        print("=" * 60)
        print(len(chunks))

    print("\nFIRST CHUNK")
    print("=" * 60)
    print(chunks[0])


if __name__ == "__main__":
    main()