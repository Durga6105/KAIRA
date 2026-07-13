"""
Structured Pipeline

Coordinates the complete structured data ingestion workflow.
"""

import json
from pathlib import Path

import pandas as pd

from llm.gemini_client import GeminiClient

from ingestion.schema_generator import SchemaGenerator
from structured.metadata_extractor import MetadataExtractor
from structured.entity_extractor import EntityExtractor
from structured.relationship_extractor import RelationshipExtractor
from structured.entity_graph_builder import EntityGraphBuilder

from utils.logger import get_logger

logger = get_logger(__name__)


class StructuredPipeline:
    """
    End-to-end structured data processing pipeline.
    """

    def __init__(self):

        # Shared Gemini Client
        self.gemini = GeminiClient()

        self.metadata_extractor = MetadataExtractor()

        self.schema_generator = SchemaGenerator(
            self.gemini
        )

        self.entity_extractor = EntityExtractor(
            self.gemini
        )

        self.relationship_extractor = RelationshipExtractor(
            self.gemini
        )

        self.graph_builder = EntityGraphBuilder()

    def process(
        self,
        file_path: str
    ) -> dict:
        """
        Process a structured document.
        """

        logger.info(
            f"Processing structured file: {file_path}"
        )

        # ----------------------------------
        # Metadata
        # ----------------------------------

        metadata = self.metadata_extractor.extract(
            file_path
        )

        # ----------------------------------
        # Read records
        # ----------------------------------

        records = self._read_file(
            file_path
        )

        metadata["record_count"] = len(records)

        metadata["column_count"] = (
            len(records[0]) if records else 0
        )

        # ----------------------------------
        # Schema Generation
        # ----------------------------------

        schema = self.schema_generator.generate(
            json.dumps(
                records[:10],
                indent=2
            )
        )

        # ----------------------------------
        # Entity Extraction
        # ----------------------------------

        entities = self.entity_extractor.extract(
            records
        )

        # ----------------------------------
        # Relationship Extraction
        # ----------------------------------

        relationships = self.relationship_extractor.extract(
            records,
            entities
        )

        # ----------------------------------
        # Graph Building
        # ----------------------------------

        graph = self.graph_builder.build(
            metadata,
            schema,
            entities,
            relationships
        )

        # ----------------------------------
        # Structured Chunks
        # ----------------------------------

        chunks = []

        for index, record in enumerate(
            records,
            start=1
        ):

            content = "\n".join(
                f"{key}: {value}"
                for key, value in record.items()
                if value is not None
            )

            chunks.append(
                {
                    "chunk_id": f"{metadata['document_stem']}_{index}",
                    "document_name": metadata["document_name"],
                    "chunk_number": index,
                    "section": "Record",
                    "content": content,
                    "word_count": len(content.split()),
                    "character_count": len(content)
                }
            )

        logger.info(
            "Structured pipeline completed successfully."
        )

        graph["chunks"] = chunks

        return graph

    def _read_file(
        self,
        file_path: str
    ) -> list[dict]:
        """
        Read any structured file into a list of records.
        """

        path = Path(file_path)

        extension = path.suffix.lower()

        if extension == ".json":

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            if isinstance(data, dict):

                first_key = next(iter(data))

                if isinstance(data[first_key], list):

                    return data[first_key]

            if isinstance(data, list):

                return data

            return [data]

        elif extension == ".csv":

            df = pd.read_csv(path)

            return df.to_dict(
                orient="records"
            )

        elif extension in [
            ".xlsx",
            ".xls"
        ]:

            df = pd.read_excel(path)

            return df.to_dict(
                orient="records"
            )

        raise ValueError(
            f"Unsupported structured file: {extension}"
        )