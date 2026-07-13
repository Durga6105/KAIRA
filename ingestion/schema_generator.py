"""
Schema Generator

Uses Gemini to infer the logical schema
of structured datasets.
"""

from llm.prompts import Prompts
from utils.json_utils import JSONUtils
from utils.logger import get_logger

logger = get_logger(__name__)


class SchemaGenerator:
    """
    Generates a logical schema for structured datasets.
    """

    def __init__(self, gemini):

        self.gemini = gemini

    def generate(
        self,
        sample_data: str
    ) -> dict:
        """
        Generate a logical schema from sample records.

        Args:
            sample_data: JSON string containing sample records.

        Returns:
            Parsed schema dictionary.
        """

        if not sample_data:

            logger.warning(
                "No sample data provided for schema generation."
            )

            return {}

        logger.info(
            "Generating schema using Gemini..."
        )

        prompt = Prompts.SCHEMA_GENERATION.format(
            data=sample_data
        )

        response = self.gemini.generate(prompt)

        schema = JSONUtils.parse(response)

        logger.info(
            "Schema generated successfully."
        )

        return schema