"""
Retrieval Agent

Coordinates the complete retrieval workflow.
"""

from llm.gemini_client import GeminiClient

from retrieval.intent_classifier import IntentClassifier
from retrieval.entity_identifier import EntityIdentifier
from retrieval.query_planner import QueryPlanner
from retrieval.hybrid_retriever import HybridRetriever
from retrieval.context_builder import ContextBuilder
from retrieval.answer_generator import AnswerGenerator

from graph.schema_loader import SchemaLoader

from utils.logger import get_logger

logger = get_logger(__name__)


class RetrievalAgent:
    """
    Coordinates the retrieval workflow.
    """

    def __init__(self):

        self.gemini = GeminiClient()

        self.intent_classifier = IntentClassifier(
            self.gemini
        )

        self.entity_identifier = EntityIdentifier(
            self.gemini
        )

        self.query_planner = QueryPlanner(
            self.gemini
        )

        self.hybrid_retriever = HybridRetriever()

        self.context_builder = ContextBuilder()

        self.answer_generator = AnswerGenerator(
            self.gemini
        )

    def query(
        self,
        question: str
    ) -> str:
        """
        Answer a user question.
        """

        logger.info(
            f"Question: {question}"
        )

        # ----------------------------------
        # Intent Classification
        # ----------------------------------

        intent = self.intent_classifier.classify(
            question
        )

        # ----------------------------------
        # Entity Identification
        # ----------------------------------

        entities = self.entity_identifier.extract(
            question
        )

        # ----------------------------------
        # Load Graph Schema
        # ----------------------------------

        schema = SchemaLoader().load()

        # ----------------------------------
        # Query Planning
        # ----------------------------------

        cypher = self.query_planner.plan(
            question,
            intent,
            entities,
            schema
        )

        # ----------------------------------
        # Hybrid Retrieval
        # ----------------------------------

        results = self.hybrid_retriever.retrieve(
            cypher=cypher,
            query=question
        )

        # ----------------------------------
        # Context Building
        # ----------------------------------

        context = self.context_builder.build(
            results
        )

        # ----------------------------------
        # Answer Generation
        # ----------------------------------

        answer = self.answer_generator.generate(
            question,
            context
        )

        return answer