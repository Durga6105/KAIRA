"""
Application Configuration

Loads and validates all environment variables required by KAIRA.
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings:
    """Application Settings"""

    # =====================================================
    # Gemini Configuration
    # =====================================================
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

    # =====================================================
    # Neo4j Aura Configuration
    # =====================================================
    NEO4J_URI: str = os.getenv("NEO4J_URI", "")
    NEO4J_USERNAME: str = os.getenv("NEO4J_USERNAME", "")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "")

    # =====================================================
    # Logging
    # =====================================================
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # =====================================================
    # Project Directories
    # =====================================================
    BASE_DIR: Path = BASE_DIR

    DATA_DIR: Path = BASE_DIR / "data"

    CHROMA_DB_PATH: Path = DATA_DIR / "chroma_db"
    CHUNKS_DIR: Path = DATA_DIR / "chunks"
    GRAPHS_DIR: Path = DATA_DIR / "graphs"
    PROCESSED_DIR: Path = DATA_DIR / "processed"
    LOGS_DIR: Path = DATA_DIR / "logs"

    UPLOAD_DIR: Path = BASE_DIR / "uploads"
    STRUCTURED_UPLOAD_DIR: Path = UPLOAD_DIR / "structured"
    UNSTRUCTURED_UPLOAD_DIR: Path = UPLOAD_DIR / "unstructured"

    def create_directories(self) -> None:
        """
        Create all required project directories.
        """

        directories = [
            self.DATA_DIR,
            self.CHROMA_DB_PATH,
            self.CHUNKS_DIR,
            self.GRAPHS_DIR,
            self.PROCESSED_DIR,
            self.LOGS_DIR,
            self.UPLOAD_DIR,
            self.STRUCTURED_UPLOAD_DIR,
            self.UNSTRUCTURED_UPLOAD_DIR,
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

    def validate(self) -> None:
        """
        Validate required environment variables.
        """

        required = {
            "GEMINI_API_KEY": self.GEMINI_API_KEY,
            "NEO4J_URI": self.NEO4J_URI,
            "NEO4J_USERNAME": self.NEO4J_USERNAME,
            "NEO4J_PASSWORD": self.NEO4J_PASSWORD,
        }

        missing = [key for key, value in required.items() if not value]

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )


# Singleton Settings Object
settings = Settings()

# Create project directories
settings.create_directories()

# Validate environment variables
settings.validate()