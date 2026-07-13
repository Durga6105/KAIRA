"""
Entity Identifier

Extracts entities from the user's query.
"""

from llm.prompts import Prompts
from utils.json_utils import JSONUtils
from utils.logger import get_logger

logger = get_logger(__name__)


class EntityIdentifier:

    def __init__(
        self,
        gemini
    ):

        self.gemini = gemini

    def extract(
        self,
        question: str
    ) -> list:

        logger.info(
            "Identifying entities..."
        )

        prompt = Prompts.ENTITY_IDENTIFICATION.format(
            question=question
        )

        response = self.gemini.generate(
            prompt
        )

        data = JSONUtils.parse(
            response
        )

        entities = data.get(
            "entities",
            []
        )

        logger.info(
            f"Extracted {len(entities)} entities."
        )

        return entities