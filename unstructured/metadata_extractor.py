"""
Unstructured Metadata Extractor

Extracts metadata from PDF, DOCX and PPTX documents.
"""

from pathlib import Path

from docling.document_converter import DocumentConverter

from utils.logger import get_logger

logger = get_logger(__name__)


class MetadataExtractor:
    """
    Extract metadata from unstructured documents.
    """

    def __init__(self):

        self.converter = DocumentConverter()

    def extract(self, file_path: str) -> dict:
        """
        Extract document metadata.

        Args:
            file_path: Path to document.

        Returns:
            Metadata dictionary.
        """

        path = Path(file_path)

        if not path.exists():

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        logger.info(
            f"Extracting metadata from {path.name}..."
        )

        result = self.converter.convert(
            str(path)
        )

        document = result.document

        text = document.export_to_markdown()

        metadata = {
            "document_name": path.name,
            "document_stem": path.stem,
            "file_extension": path.suffix.lower(),
            "file_size": path.stat().st_size,
            "file_type": "unstructured",
            "character_count": len(text),
            "word_count": len(text.split())
        }

        # PDF
        if path.suffix.lower() == ".pdf":

            metadata["page_count"] = len(
                getattr(document, "pages", [])
            )

        # PPTX
        elif path.suffix.lower() == ".pptx":

            metadata["slide_count"] = len(
                getattr(document, "pages", [])
            )

        # DOCX
        elif path.suffix.lower() == ".docx":

            metadata["page_count"] = None

        logger.info(
            "Metadata extraction completed."
        )

        return metadata