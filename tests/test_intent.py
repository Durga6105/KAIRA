import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from llm.gemini_client import GeminiClient
from retrieval.intent_classifier import IntentClassifier


def main():

    gemini = GeminiClient()

    classifier = IntentClassifier(
        gemini
    )

    questions = [

        "What is Jane Doe's email?",

        "Summarize the Budget 2026 document.",

        "Who approves expenditures above 10 lakhs?"
    ]

    for question in questions:

        print()

        print(question)

        print(
            classifier.classify(
                question
            )
        )


if __name__ == "__main__":
    main()