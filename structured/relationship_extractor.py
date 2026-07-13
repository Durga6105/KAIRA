"""
Structured Relationship Extractor

Uses rule-based extraction for document hierarchies
and Gemini for other structured datasets.
"""

import json

from llm.prompts import Prompts
from utils.json_utils import JSONUtils
from utils.logger import get_logger

logger = get_logger(__name__)


class RelationshipExtractor:
    """
    Hybrid relationship extractor.
    """

    def __init__(self, gemini):

        self.gemini = gemini

    def extract(
        self,
        records: list[dict],
        entities: list[dict]
    ) -> list:
        """
        Extract relationships from structured records.
        """

        if not records:

            logger.warning(
                "No records found for relationship extraction."
            )

            return []

        if not entities:

            logger.warning(
                "No entities found for relationship extraction."
            )

            return []

        # ------------------------------------
        # Excel / Document Hierarchy
        # ------------------------------------

        if self._is_document_hierarchy(records):

            logger.info(
                "Detected document hierarchy. Using rule-based relationship extraction."
            )

            return self._build_hierarchy_relationships(records)

        # ------------------------------------
        # JSON / Other Structured Files
        # ------------------------------------

        logger.info(
            f"Extracting relationships from {len(entities)} entities using Gemini..."
        )

        prompt = Prompts.RELATIONSHIP_EXTRACTION.format(
            records=json.dumps(records, indent=2),
            entities=json.dumps(entities, indent=2)
        )

        response = self.gemini.generate(prompt)

        result = JSONUtils.parse(response)

        if not isinstance(result, dict):

            logger.warning(
                "Invalid relationship extraction response."
            )

            return []

        relationships = result.get(
            "relationships",
            []
        )

        return self._remove_duplicates(
            relationships
        )

    def _is_document_hierarchy(
        self,
        records: list[dict]
    ) -> bool:
        """
        Detect document hierarchy datasets.
        """

        if not records:
            return False

        keys = {
            key.lower()
            for key in records[0].keys()
        }

        required = {
            "folder",
            "subfolder",
            "filename",
            "category"
        }

        return required.issubset(keys)

    def _build_hierarchy_relationships(
        self,
        records: list[dict]
    ) -> list:
        """
        Build hierarchy relationships without an LLM.
        """

        relationships = []
        seen = set()

        for record in records:

            folder = record.get("Folder")
            subfolder = record.get("Subfolder")
            document = record.get("Filename")
            category = record.get("Category")

            pairs = [

                (folder, subfolder, "CONTAINS"),

                (subfolder, document, "CONTAINS"),

                (document, category, "BELONGS_TO")

            ]

            for source, target, relation in pairs:

                if not source or not target:
                    continue

                key = (
                    source,
                    target,
                    relation
                )

                if key in seen:
                    continue

                seen.add(key)

                relationships.append({

                    "source": source,

                    "target": target,

                    "type": relation,

                    "properties": {}

                })

        logger.info(
            f"Built {len(relationships)} hierarchy relationships."
        )

        return relationships

    def _remove_duplicates(
        self,
        relationships: list
    ) -> list:
        """
        Remove duplicate relationships.
        """

        unique = []
        seen = set()

        for relationship in relationships:

            if not isinstance(
                relationship,
                dict
            ):
                continue

            source = relationship.get("source")
            target = relationship.get("target")
            relation = relationship.get("type")

            if not source or not target or not relation:
                continue

            key = (

                source.strip().lower(),

                target.strip().lower(),

                relation.strip().upper()

            )

            if key in seen:
                continue

            seen.add(key)

            unique.append({

                "source": source,

                "target": target,

                "type": relation,

                "properties": relationship.get(
                    "properties",
                    {}
                )

            })

        logger.info(
            f"Extracted {len(unique)} unique relationships."
        )

        return unique