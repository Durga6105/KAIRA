import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from google import genai
from config.settings import settings


def main():

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    print("\nAvailable Gemini Models")
    print("=" * 80)

    for model in client.models.list():

        print(model.name)

        if hasattr(model, "supported_actions"):
            print("Actions :", model.supported_actions)

        elif hasattr(model, "supported_generation_methods"):
            print("Methods :", model.supported_generation_methods)

        print("-" * 80)


if __name__ == "__main__":
    main()