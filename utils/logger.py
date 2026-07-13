"""
Centralized Logging Utility for KAIRA.
"""

import logging
from pathlib import Path

from config.settings import settings


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Args:
        name (str): Name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """

    logger = logging.getLogger(name)

    # Avoid duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    # ==========================
    # Log Format
    # ==========================
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ==========================
    # Console Handler
    # ==========================
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # ==========================
    # File Handler
    # ==========================
    log_file = Path(settings.LOGS_DIR) / "kaira.log"

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    # ==========================
    # Add Handlers
    # ==========================
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger