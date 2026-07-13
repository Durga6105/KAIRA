import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from llm.gemini_client import GeminiClient


def main():

    gemini = GeminiClient()

    print("\nChecking Gemini Connection...\n")

    if gemini.health_check():
        print("✅ Gemini Connected Successfully")
    else:
        print("❌ Gemini Connection Failed")

    print("\nSample Response:\n")

    response = gemini.generate(
        "Explain Knowledge Graph in one sentence."
    )

    print(response)


if __name__ == "__main__":
    main()