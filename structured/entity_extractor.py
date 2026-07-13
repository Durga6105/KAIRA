"""
Structured Entity Extractor

Uses Gemini to extract entities from structured
records (primarily JSON).
"""

import json

from llm.prompts import Prompts
from utils.json_utils import JSONUtils
from utils.logger import get_logger

logger = get_logger(__name__)


class EntityExtractor:
    """
    LLM-based structured entity extractor.
    """

    def __init__(self, gemini):

        self.gemini = gemini

    def extract(
        self,
        records: list[dict]
    ) -> list:
        """
        Extract entities from structured records.

        Args:
            records: List of structured records.

        Returns:
            List of extracted entities.
        """

        if not records:

            logger.warning("No records found for entity extraction.")

            return []

        logger.info(
            f"Extracting entities from {len(records)} records..."
        )

        prompt = Prompts.ENTITY_EXTRACTION.format(
            data=json.dumps(records, indent=2)
        )

        response = self.gemini.generate(prompt)

        result = JSONUtils.parse(response)

        entities = result.get("entities", [])

        logger.info(
            f"Extracted {len(entities)} entities."
        )

        return entities