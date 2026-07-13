import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from llm.gemini_client import GeminiClient
from retrieval.entity_identifier import EntityIdentifier


def main():

    gemini = GeminiClient()

    identifier = EntityIdentifier(
        gemini
    )

    questions = [

        "What is Jane Doe's email?",

        "Who approves Budget 2026?",

        "Show Finance policies."
    ]

    for question in questions:

        print()

        print(question)

        print(
            identifier.extract(
                question
            )
        )


if __name__ == "__main__":
    main()