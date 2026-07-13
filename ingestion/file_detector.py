"""
File Detector

Detects uploaded file and validates its existence.
"""

from pathlib import Path

from utils.logger import get_logger

logger = get_logger(__name__)


class FileDetector:
    """
    Detect uploaded file.
    """

    @staticmethod
    def detect(file_path: str) -> str:
        """
        Detect file extension.

        Returns:
            File extension (e.g. ".pdf", ".json")
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        extension = path.suffix.lower()

        logger.info(
            f"Detected extension: {extension}"
        )

        return extension