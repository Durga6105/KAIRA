import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from embeddings.embedding_generator import (
    EmbeddingGenerator
)


def main():

    generator = EmbeddingGenerator()

    vector = generator.generate(
        "Annual Budget 2026"
    )

    print(len(vector))


if __name__ == "__main__":
    main()