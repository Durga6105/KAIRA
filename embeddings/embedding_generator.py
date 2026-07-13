"""
Embedding Generator

Generates embeddings using Gemini.
"""

from google import genai

from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class EmbeddingGenerator:
    """
    Gemini embedding generator.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = "models/gemini-embedding-001"

    def generate(
        self,
        text: str
    ) -> list[float]:

        logger.info(
            "Generating embedding..."
        )

        response = self.client.models.embed_content(
            model=self.model,
            contents=text
        )

        return response.embeddings[0].values