import os
import sys

from loguru import logger

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)


def configure_logging() -> None:
    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        enqueue=True,
        backtrace=True,
        diagnose=False,
    )

    logger.add(
        "logs/backend.log",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        enqueue=True,
        level="INFO",
    )


def get_logger(name: str):
    return logger.bind(module=name)
