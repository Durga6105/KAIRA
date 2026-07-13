"""
Context Builder

Builds the final context for answer generation.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class ContextBuilder:
    """
    Combines graph and vector retrieval results.
    """

    def build(
        self,
        results: dict
    ) -> str:

        logger.info(
            "Building context..."
        )

        context = []

        # -------------------------
        # Graph Results
        # -------------------------

        graph_results = results.get(
            "graph",
            []
        )

        if graph_results:

            context.append(
                "GRAPH RESULTS\n"
            )

            for record in graph_results:

                context.append(
                    str(record)
                )

        # -------------------------
        # Vector Results
        # -------------------------

        vector_results = results.get(
            "vector",
            {}
        )

        documents = vector_results.get(
            "documents",
            []
        )

        if documents:

            context.append(
                "\nVECTOR RESULTS\n"
            )

            for group in documents:

                for chunk in group:

                    context.append(
                        chunk
                    )

        logger.info(
            "Context built successfully."
        )

        return "\n\n".join(context)