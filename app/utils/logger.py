import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Create logs directory if it doesn't exist
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Create logger
logger = logging.getLogger("SnapPDF")
logger.setLevel(logging.DEBUG)

# Create formatters
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
console_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)-8s - %(message)s", datefmt="%H:%M:%S"
)

# File handler (rotates when file reaches 5MB, keeps 3 backup files)
file_handler = RotatingFileHandler(
    log_dir / "snappdf.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def get_logger(name=None):
    """Get a logger with the given name.

    Args:
        name (str, optional): Name of the logger. If None, returns the root logger.

    Returns:
        logging.Logger: Configured logger instance.
    """
    if name:
        return logging.getLogger(f"SnapPDF.{name}")
    return logger
