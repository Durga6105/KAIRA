"""
Query Planner

Generates Cypher queries using Gemini.
"""

import json

from llm.prompts import Prompts
from utils.json_utils import JSONUtils
from utils.logger import get_logger

logger = get_logger(__name__)


class QueryPlanner:

    def __init__(self, gemini):

        self.gemini = gemini

    def plan(
        self,
        question: str,
        intent: str,
        entities: list,
        schema: str
    ) -> str:

        logger.info(
            "Generating Cypher query..."
        )

        prompt = Prompts.QUERY_PLANNER.format(
            question=question,
            intent=intent,
            entities=json.dumps(
                entities,
                indent=2
            ),
            schema=schema
        )

        response = self.gemini.generate(
            prompt
        )

        data = JSONUtils.parse(
            response
        )

        cypher = data.get(
            "cypher",
            ""
        )

        logger.info(
            "Cypher generated successfully."
        )

        return cypher