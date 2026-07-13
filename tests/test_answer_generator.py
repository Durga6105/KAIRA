import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from llm.gemini_client import GeminiClient
from retrieval.answer_generator import AnswerGenerator


def main():

    gemini = GeminiClient()

    generator = AnswerGenerator(
        gemini
    )

    context = """
GRAPH RESULTS

Person: Jane Doe
Email: jane.doe@company.com

Person: John Smith
Department: Finance

VECTOR RESULTS

Budget approval requires CFO approval.

Budget 2026 total allocation is INR 45 Crores.

Finance reviews expenditures above INR 10 Lakhs.
"""

    question = "What is Jane Doe's email?"

    answer = generator.generate(
        question,
        context
    )

    print()

    print("=" * 60)
    print("QUESTION")
    print("=" * 60)

    print(question)

    print()

    print("=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(answer)


if __name__ == "__main__":
    main()