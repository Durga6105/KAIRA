import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from retrieval.context_builder import ContextBuilder


def main():

    builder = ContextBuilder()

    results = {

        "graph": [

            {
                "person": "Jane Doe",
                "email": "jane.doe@company.com"
            },

            {
                "person": "John Smith",
                "department": "Finance"
            }

        ],

        "vector": {

            "documents": [

                [

                    "Budget approval requires CFO approval.",

                    "Budget 2026 total allocation is INR 45 Crores.",

                    "Finance department reviews all expenditures."

                ]

            ]

        }

    }

    context = builder.build(results)

    print()

    print("=" * 60)
    print("CONTEXT")
    print("=" * 60)

    print(context)


if __name__ == "__main__":
    main()