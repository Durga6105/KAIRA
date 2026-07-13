import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from unstructured.metadata_extractor import MetadataExtractor


def main():

    extractor = MetadataExtractor()

    metadata = extractor.extract(
        "uploads/unstructured/DecisionIntelligencePlatform.pptx"
    )

    print("\nMETADATA")
    print("=" * 60)

    for key, value in metadata.items():
        print(f"{key:20}: {value}")


if __name__ == "__main__":
    main()