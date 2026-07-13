"""
Semantic Chunker
"""

import uuid

from utils.logger import get_logger

logger = get_logger(__name__)


class Chunker:
    """
    Creates semantic chunks from extracted text.
    """

    def chunk(
        self,
        document: dict
    ) -> list[dict]:

        logger.info(
            f"Chunking {document['document_name']}..."
        )

        sections = self._split_sections(
            document["content"]
        )

        chunks = []

        for index, section in enumerate(sections, start=1):

            section = section.strip()

            if not section:
                continue

            lines = section.splitlines()

            title = (
                lines[0]
                .replace("#", "")
                .strip()
            )

            chunks.append(
                {
                    "chunk_id": str(uuid.uuid4()),
                    "document_name": document["document_name"],
                    "chunk_number": index,
                    "section": title,
                    "content": section,
                    "word_count": len(section.split()),
                    "character_count": len(section)
                }
            )

        logger.info(
            f"Created {len(chunks)} chunks."
        )

        return chunks

    def _split_sections(
        self,
        text: str
    ) -> list[str]:

        sections = []

        current = []

        for line in text.splitlines():

            if line.startswith("#") and current:

                sections.append(
                    "\n".join(current)
                )

                current = []

            current.append(line)

        if current:

            sections.append(
                "\n".join(current)
            )

        return sections