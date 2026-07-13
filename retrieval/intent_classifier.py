"""
Intent Classifier

Uses Gemini to classify user intent.
"""

from llm.prompts import Prompts
from utils.json_utils import JSONUtils
from utils.logger import get_logger

logger = get_logger(__name__)


class IntentClassifier:

    def __init__(
        self,
        gemini
    ):

        self.gemini = gemini

    def classify(
        self,
        question: str
    ) -> str:

        logger.info(
            "Classifying intent..."
        )

        prompt = Prompts.INTENT_CLASSIFICATION.format(
            question=question
        )

        response = self.gemini.generate(
            prompt
        )

        data = JSONUtils.parse(
            response
        )

        intent = data.get(
            "intent",
            "HYBRID"
        ).upper()

        logger.info(
            f"Intent: {intent}"
        )

        return intent