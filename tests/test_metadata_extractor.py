import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from structured.metadata_extractor import MetadataExtractor


def main():

    file_path = "uploads/structured/document.xlsx"

    metadata = MetadataExtractor.extract(file_path)

    print("\nStructured Metadata\n")
    print("=" * 50)

    for key, value in metadata.items():
        print(f"{key:<20}: {value}")


if __name__ == "__main__":
    main()