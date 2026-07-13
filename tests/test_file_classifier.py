import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ingestion.file_classifier import FileClassifier


def main():

    extensions = [
        ".json",
        ".xlsx",
        ".csv",
        ".pdf",
        ".docx",
        ".pptx",
        ".txt",
        ".zip",
        ".exe",
    ]

    print("=" * 50)

    for extension in extensions:

        category = FileClassifier.classify(extension)

        print(f"{extension:<10} -> {category}")

    print("=" * 50)


if __name__ == "__main__":
    main()