import sys
from pathlib import Path

from loguru import logger

LOG_DIRECTORY = Path("logs")

LOG_DIRECTORY.mkdir(
    exist_ok=True,
)


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
        LOG_DIRECTORY / "fuhrer.log",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        enqueue=True,
        level="INFO",
    )


def get_logger(name: str):

    return logger.bind(module=name)
