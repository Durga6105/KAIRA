"""
Structured Metadata Extractor

Extracts metadata from structured files.
"""

from pathlib import Path

import pandas as pd


class MetadataExtractor:
    """
    Extract metadata from structured files.
    """

    @staticmethod
    def extract(file_path: str) -> dict:

        path = Path(file_path)

        metadata = {
            "document_name": path.name,
            "document_stem": path.stem,
            "file_extension": path.suffix.lower(),
            "file_size": path.stat().st_size,
            "file_type": "structured",
        }

        # Excel
        if path.suffix.lower() in [".xlsx", ".xls"]:

            excel = pd.ExcelFile(path)

            metadata["sheet_count"] = len(excel.sheet_names)
            metadata["sheet_names"] = excel.sheet_names

        # CSV / JSON
        else:

            metadata["record_count"] = 0

        return metadata