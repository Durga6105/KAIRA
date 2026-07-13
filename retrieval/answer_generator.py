"""
Answer Generator

Generates the final answer using Gemini.
"""

from llm.prompts import Prompts
from utils.logger import get_logger

logger = get_logger(__name__)


class AnswerGenerator:
    """
    Generates answers from retrieved context.
    """

    def __init__(
        self,
        gemini
    ):

        self.gemini = gemini

    def generate(
        self,
        question: str,
        context: str
    ) -> str:

        logger.info(
            "Generating answer..."
        )

        prompt = Prompts.ANSWER_GENERATION.format(
            context=context,
            question=question
        )

        answer = self.gemini.generate(
            prompt
        )

        logger.info(
            "Answer generated successfully."
        )

        return answer.strip()