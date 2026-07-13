"""
File Classifier

Classifies files into Structured or Unstructured categories.
"""

from utils.constants import (
    STRUCTURED_FILE_TYPES,
    UNSTRUCTURED_FILE_TYPES,
)


class FileClassifier:
    """
    Classifies uploaded files.
    """

    @staticmethod
    def classify(file_extension: str) -> str:
        """
        Classify a file based on its extension.

        Returns:
            structured
            unstructured
            unsupported
        """

        file_extension = file_extension.lower()

        if file_extension in STRUCTURED_FILE_TYPES:
            return "structured"

        if file_extension in UNSTRUCTURED_FILE_TYPES:
            return "unstructured"

        return "unsupported"