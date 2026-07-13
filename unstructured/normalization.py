"""
Entity Normalization

Normalizes extracted entities and relationships.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class Normalizer:
    """
    Normalizes entities and relationships.
    """

    def normalize(
        self,
        entities: list,
        relationships: list
    ) -> tuple[list, list]:

        logger.info("Normalizing entities and relationships...")

        normalized_entities = []

        for entity in entities:

            normalized_entities.append(
                {
                    "type": entity["type"].strip(),
                    "name": " ".join(
                        entity["name"].split()
                    ).title(),
                    "properties": entity.get(
                        "properties",
                        {}
                    )
                }
            )

        normalized_relationships = []

        for relationship in relationships:

            normalized_relationships.append(
                {
                    "source": " ".join(
                        relationship["source"].split()
                    ).title(),

                    "target": " ".join(
                        relationship["target"].split()
                    ).title(),

                    "type": relationship["type"]
                    .strip()
                    .upper(),

                    "properties": relationship.get(
                        "properties",
                        {}
                    )
                }
            )

        logger.info(
            "Normalization completed."
        )

        return (
            normalized_entities,
            normalized_relationships
        )