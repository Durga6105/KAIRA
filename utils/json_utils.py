"""
JSON Utilities

Provides helper functions for safely parsing and cleaning
LLM-generated JSON responses.
"""

import json

from utils.logger import get_logger

logger = get_logger(__name__)


class JSONUtils:
    """
    Utility methods for JSON parsing.
    """

    @staticmethod
    def clean_json(text: str) -> str:
        """
        Remove markdown code fences from LLM responses.
        """

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.startswith("```"):
            text = text.replace("```", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        return text.strip()

    @staticmethod
    def parse(text: str) -> dict:
        """
        Safely parse JSON.
        """

        try:

            cleaned = JSONUtils.clean_json(text)

            return json.loads(cleaned)

        except json.JSONDecodeError as e:

            logger.error(f"Invalid JSON: {e}")

            raise ValueError(
                f"Failed to parse JSON:\n{cleaned}"
            )