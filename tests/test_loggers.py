import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.logger import get_logger


def main():

    logger = get_logger("KAIRA-Test")

    logger.info("Logger initialized successfully.")

    logger.warning("This is a warning message.")

    logger.error("This is an error message.")

    print("\n✅ Logger test completed.")


if __name__ == "__main__":
    main()