"""
Unstructured Pipeline

Coordinates the complete unstructured document ingestion workflow.
"""

from unstructured.text_extractor import TextExtractor
from unstructured.metadata_extractor import MetadataExtractor
from unstructured.chunker import Chunker
from unstructured.lexical_graph_builder import LexicalGraphBuilder
from unstructured.entity_extractor import EntityExtractor
from unstructured.relationship_extractor import RelationshipExtractor
from unstructured.normalization import Normalizer
from unstructured.deduplication import Deduplicator
from unstructured.entity_graph_builder import EntityGraphBuilder

from llm.gemini_client import GeminiClient
from utils.logger import get_logger

logger = get_logger(__name__)


class UnstructuredPipeline:
    """
    End-to-end unstructured data pipeline.
    """

    def __init__(self):

        gemini = GeminiClient()

        self.text_extractor = TextExtractor()
        self.metadata_extractor = MetadataExtractor()
        self.chunker = Chunker()

        self.lexical_graph_builder = (
            LexicalGraphBuilder()
        )

        self.entity_extractor = (
            EntityExtractor(gemini)
        )

        self.relationship_extractor = (
            RelationshipExtractor(gemini)
        )

        self.normalizer = Normalizer()

        self.deduplicator = Deduplicator()

        self.entity_graph_builder = (
            EntityGraphBuilder()
        )

    def process(
        self,
        file_path: str
    ) -> dict:
        """
        Process an unstructured document.
        """

        logger.info(
            f"Processing unstructured file: {file_path}"
        )

        # -------------------------
        # Text Extraction
        # -------------------------

        document = self.text_extractor.extract(
            file_path
        )

        # -------------------------
        # Metadata
        # -------------------------

        metadata = self.metadata_extractor.extract(
            file_path
        )

        # -------------------------
        # Chunking
        # -------------------------

        chunks = self.chunker.chunk(
            document
        )

        # -------------------------
        # Lexical Graph
        # -------------------------

        lexical_graph = (
            self.lexical_graph_builder.build(
                metadata,
                chunks
            )
        )

        # -------------------------
        # Entity Extraction
        # -------------------------

        entities = (
            self.entity_extractor.extract(
                chunks
            )
        )

        # -------------------------
        # Relationship Extraction
        # -------------------------

        relationships = (
            self.relationship_extractor.extract(
                chunks,
                entities
            )
        )

        # -------------------------
        # Normalization
        # -------------------------

        entities, relationships = (
            self.normalizer.normalize(
                entities,
                relationships
            )
        )

        # -------------------------
        # Deduplication
        # -------------------------

        entities, relationships = (
            self.deduplicator.deduplicate(
                entities,
                relationships
            )
        )

        # -------------------------
        # Entity Graph
        # -------------------------

        graph = (
            self.entity_graph_builder.build(
                metadata,
                lexical_graph,
                entities,
                relationships
            )
        )
        graph["chunks"] = chunks


        logger.info(
            "Unstructured pipeline completed successfully."
        )

        return graph