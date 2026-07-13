import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ingestion.file_detector import FileDetector


def main():

    files = [

        "people.json",
        "report.pdf",
        "slides.pptx",
        "employee.xlsx",
        "notes.txt",
        "restaurant.docx"

    ]

    for file in files:

        extension = FileDetector.detect(file)

        print(f"{file:<25} -> {extension}")


if __name__ == "__main__":
    main()