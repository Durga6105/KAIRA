"""
Application Constants
"""

# ==========================
# Supported Structured Files
# ==========================

STRUCTURED_FILE_TYPES = {
    ".csv",
    ".xlsx",
    ".xls",
    ".json",
}

# ==========================
# Supported Unstructured Files
# ==========================

UNSTRUCTURED_FILE_TYPES = {
    ".pdf",
    ".docx",
    ".pptx",
    ".txt",
}

# ==========================
# Chunking
# ==========================

DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200

# ==========================
# Graph Labels
# ==========================

DOCUMENT_NODE = "Document"
ENTITY_NODE = "Entity"

# ==========================
# Relationship Labels
# ==========================

MENTIONS = "MENTIONS"
RELATED_TO = "RELATED_TO"