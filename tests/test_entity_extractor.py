import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))

from llm.gemini_client import GeminiClient
from structured.entity_extractor import EntityExtractor


def main():

    file_path = "uploads/structured/employee.json"

    df = pd.read_json(file_path)

    records = df.to_dict(orient="records")

    gemini = GeminiClient()

    extractor = EntityExtractor(gemini)

    entities = extractor.extract(records)

    print("\nExtracted Entities")
    print("=" * 60)
    print(f"Total Entities: {len(entities)}\n")

    for entity in entities:
        print(entity)


if __name__ == "__main__":
    main()