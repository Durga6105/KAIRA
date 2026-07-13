"""
Unstructured Text Extractor

Extracts text from PDF, DOCX and PPTX using Docling.
"""

from pathlib import Path

from docling.document_converter import DocumentConverter

from utils.logger import get_logger

logger = get_logger(__name__)


class TextExtractor:
    """
    Extract text from unstructured documents.
    """

    def __init__(self):

        self.converter = DocumentConverter()

    def extract(self, file_path: str) -> dict:
        """
        Extract text from an unstructured document.

        Args:
            file_path: Path to document.

        Returns:
            Dictionary containing extracted text.
        """

        path = Path(file_path)

        if not path.exists():

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        logger.info(
            f"Extracting text from {path.name}..."
        )

        try:

            result = self.converter.convert(
                str(path)
            )

            document = result.document

            text = document.export_to_markdown()

            logger.info(
                f"Successfully extracted text from {path.name}"
            )

            return {
                "document_name": path.name,
                "document_stem": path.stem,
                "file_extension": path.suffix.lower(),
                "content": text
            }

        except Exception as e:

            logger.exception(
                f"Failed to extract text from {path.name}"
            )

            raise RuntimeError(
                f"Text extraction failed: {e}"
            )