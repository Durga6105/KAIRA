"""
Entity Deduplication

Removes duplicate entities and relationships.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class Deduplicator:
    """
    Removes duplicate entities and relationships.
    """

    def deduplicate(
        self,
        entities: list,
        relationships: list
    ) -> tuple[list, list]:

        logger.info(
            "Removing duplicate entities and relationships..."
        )

        unique_entities = []

        seen_entities = set()

        for entity in entities:

            key = (
                entity["type"].lower(),
                entity["name"].lower()
            )

            if key in seen_entities:
                continue

            seen_entities.add(key)

            unique_entities.append(entity)

        unique_relationships = []

        seen_relationships = set()

        for relationship in relationships:

            key = (
                relationship["source"].lower(),
                relationship["target"].lower(),
                relationship["type"].upper()
            )

            if key in seen_relationships:
                continue

            seen_relationships.add(key)

            unique_relationships.append(
                relationship
            )

        logger.info(
            f"Entities: {len(unique_entities)}"
        )

        logger.info(
            f"Relationships: {len(unique_relationships)}"
        )

        return (
            unique_entities,
            unique_relationships
        )