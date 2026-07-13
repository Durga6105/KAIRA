import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.retrieval_agent import RetrievalAgent


def main():

    agent = RetrievalAgent()

    questions = [

        "What is Jane Doe's email?",

        "Who approves expenditures above INR 10 Lakhs?",

        "Summarize the Budget 2026 document."

    ]

    for question in questions:

        print()
        print("=" * 80)
        print("QUESTION")
        print("=" * 80)
        print(question)

        try:

            answer = agent.query(
                question
            )

            print()
            print("=" * 80)
            print("ANSWER")
            print("=" * 80)
            print(answer)

        except Exception as e:

            print()
            print("ERROR")
            print(e)


if __name__ == "__main__":
    main()