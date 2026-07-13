import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from retrieval.graph_retriever import GraphRetriever


def main():

    retriever = GraphRetriever()

    cypher = """
    MATCH (p:Entity)-[r]->(e:Entity)
    WHERE p.name = "Jane Doe"
    RETURN
        p.name AS source,
        type(r) AS relationship,
        e.name AS target
    """

    results = retriever.retrieve(cypher)

    print()
    print("=" * 60)
    print("GRAPH RESULTS")
    print("=" * 60)

    if not results:
        print("No results found.")
        return

    for record in results:
        print(record)


if __name__ == "__main__":
    main()