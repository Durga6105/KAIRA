import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from graph.neo4j_client import Neo4jClient


def main():

    neo4j = Neo4jClient()

    print("\nChecking Neo4j Aura Connection...\n")

    if neo4j.health_check():

        print("✅ Neo4j Connected Successfully")

    else:

        print("❌ Neo4j Connection Failed")

    neo4j.close()


if __name__ == "__main__":
    main()