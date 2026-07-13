"""
Unstructured Entity Extractor
"""

import json

from llm.prompts import Prompts
from utils.json_utils import JSONUtils
from utils.logger import get_logger

logger = get_logger(__name__)


class EntityExtractor:

    def __init__(self, gemini):

        self.gemini = gemini

    def extract(
        self,
        chunks: list[dict]
    ) -> list:

        logger.info(
            f"Extracting entities from {len(chunks)} chunks..."
        )

        prompt = Prompts.UNSTRUCTURED_ENTITY_EXTRACTION.format(
            chunks=json.dumps(chunks, indent=2)
        )

        response = self.gemini.generate(prompt)

        result = JSONUtils.parse(response)

        entities = result.get(
            "entities",
            []
        )

        logger.info(
            f"Extracted {len(entities)} entities."
        )

        return entities