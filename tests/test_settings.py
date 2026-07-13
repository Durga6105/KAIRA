"""
Test configuration settings.
"""

from config.settings import settings


def main():
    print("=" * 50)
    print("KAIRA Configuration Test")
    print("=" * 50)

    print(f"Gemini API Key      : {'Loaded' if settings.GEMINI_API_KEY else 'Missing'}")
    print(f"Neo4j URI           : {settings.NEO4J_URI}")
    print(f"Neo4j Username      : {settings.NEO4J_USERNAME}")
    print(f"ChromaDB Path       : {settings.CHROMA_DB_PATH}")
    print(f"Upload Directory    : {settings.UPLOAD_DIR}")
    print(f"Log Directory       : {settings.LOGS_DIR}")

    print("\n✅ Configuration loaded successfully.")


if __name__ == "__main__":
    main()