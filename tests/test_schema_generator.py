import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ingestion.schema_generator import SchemaGenerator


def main():

    data = """
EmployeeID,Name,Department

101,John,Finance

102,Alice,HR

103,Bob,IT
"""

    schema = SchemaGenerator().generate(data)

    print(schema)


if __name__ == "__main__":
    main()