"""
Ingestion Agent

Coordinates the complete document ingestion workflow.
"""

from pathlib import Path

from ingestion.file_detector import FileDetector
from ingestion.file_classifier import FileClassifier

from agents.kg_builder_agent import KGBuilderAgent

from utils.logger import get_logger

logger = get_logger(__name__)


class IngestionAgent:
    """
    Master ingestion agent.
    """

    def __init__(self):

        self.detector = FileDetector()

        self.classifier = FileClassifier()

        self.builder = KGBuilderAgent()

    def ingest(
        self,
        file_path: str
    ) -> dict:
        """
        Ingest any supported document.
        """

        logger.info(
            f"Starting ingestion: {file_path}"
        )

        file_path = str(
            Path(file_path)
        )

        # -------------------------
        # Detect File
        # -------------------------

        extension = self.detector.detect(
            file_path
        )

        logger.info(
            f"Detected extension: {extension}"
        )

        # -------------------------
        # Classify
        # -------------------------

        file_type = self.classifier.classify(
            extension
        )

        logger.info(
            f"Detected type: {file_type}"
        )

        # -------------------------
        # Build Knowledge Graph
        # -------------------------

        graph = self.builder.build(
            file_path=file_path,
            file_type=file_type
        )

        logger.info(
            "Ingestion completed successfully."
        )

        return graph