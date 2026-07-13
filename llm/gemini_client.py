"""
Gemini Client

Handles all interactions with Google's Gemini API.
"""

import time

from google import genai
from google.genai import types

from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class GeminiClient:
    """
    Gemini API Client.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = settings.GEMINI_MODEL

        self.max_retries = 3

        self.base_delay = 2

        logger.info(
            "Gemini Client initialized successfully."
        )

    def generate(
        self,
        prompt: str
    ) -> str:
        """
        Generate response from Gemini with retry support.
        """

        last_error = None

        for attempt in range(
            1,
            self.max_retries + 1
        ):

            try:

                response = self.client.models.generate_content(

                    model=self.model,

                    contents=prompt,

                    config=types.GenerateContentConfig(
                        temperature=0.2,
                    ),
                )

                if not response.text:

                    raise RuntimeError(
                        "Empty response received from Gemini."
                    )

                return response.text.strip()

            except Exception as e:

                last_error = e

                logger.warning(
                    f"Gemini attempt {attempt}/{self.max_retries} failed: {e}"
                )

                if attempt < self.max_retries:

                    delay = self.base_delay ** attempt

                    logger.info(
                        f"Retrying in {delay} seconds..."
                    )

                    time.sleep(delay)

        logger.error(
            f"Gemini generation failed after {self.max_retries} attempts."
        )

        raise RuntimeError(
            f"Gemini API Error: {last_error}"
        )

    def health_check(self) -> bool:
        """
        Check whether Gemini API is working.
        """

        try:

            response = self.generate(
                "Reply with only: OK"
            )

            return response.upper() == "OK"

        except Exception:

            return False