"""
Unstructured Relationship Extractor
"""

import json

from llm.prompts import Prompts
from utils.json_utils import JSONUtils
from utils.logger import get_logger

logger = get_logger(__name__)


class RelationshipExtractor:
    """
    Extract relationships between entities from
    unstructured document chunks.
    """

    def __init__(self, gemini):

        self.gemini = gemini

    def extract(
        self,
        chunks: list[dict],
        entities: list[dict]
    ) -> list:

        if not chunks:

            logger.warning(
                "No chunks found."
            )

            return []

        if not entities:

            logger.warning(
                "No entities found."
            )

            return []

        logger.info(
            f"Extracting relationships from {len(entities)} entities..."
        )

        prompt = Prompts.UNSTRUCTURED_RELATIONSHIP_EXTRACTION.format(
            chunks=json.dumps(chunks, indent=2),
            entities=json.dumps(entities, indent=2)
        )

        response = self.gemini.generate(prompt)

        result = JSONUtils.parse(response)

        relationships = result.get(
            "relationships",
            []
        )

        unique_relationships = []

        seen = set()

        for relationship in relationships:

            source = relationship.get("source")
            target = relationship.get("target")
            relation = relationship.get("type")

            if not source or not target or not relation:
                continue

            key = (
                source.lower().strip(),
                target.lower().strip(),
                relation.upper().strip()
            )

            if key in seen:
                continue

            seen.add(key)

            unique_relationships.append(
                {
                    "source": source,
                    "target": target,
                    "type": relation,
                    "properties": relationship.get(
                        "properties",
                        {}
                    )
                }
            )

        logger.info(
            f"Extracted {len(unique_relationships)} relationships."
        )

        return unique_relationships