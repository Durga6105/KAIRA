import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from graph.schema_loader import SchemaLoader


def main():

    loader = SchemaLoader()

    schema = loader.load()

    print()

    print("=" * 60)
    print("GRAPH SCHEMA")
    print("=" * 60)

    print(schema)


if __name__ == "__main__":
    main()