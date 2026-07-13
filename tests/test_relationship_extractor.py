import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from structured.entity_extractor import EntityExtractor
from structured.relationship_extractor import RelationshipExtractor


def main():

    with open(
        "uploads/structured/employee.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    records = data["people"]

    entity_extractor = EntityExtractor()
    entities = entity_extractor.extract(records)

    relationship_extractor = RelationshipExtractor()
    relationships = relationship_extractor.extract(
        records,
        entities
    )

    print("\nExtracted Relationships\n")
    print("=" * 60)

    for relationship in relationships:
        print(relationship)


if __name__ == "__main__":
    main()