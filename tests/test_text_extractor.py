import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from unstructured.text_extractor import TextExtractor


def main():

    extractor = TextExtractor()

    result = extractor.extract(
        
        "uploads/unstructured/DecisionIntelligencePlatform.pptx"
    )

    print("\nDOCUMENT")
    print("=" * 60)
    print(result["document_name"])

    print("\nTEXT")
    print("=" * 60)
    print(result["content"][:3000])


if __name__ == "__main__":
    main()