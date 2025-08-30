import pyautogui as pg
from app.utils.logger import get_logger

logger = get_logger("screen_shot")


def capture_screen(file_name, region=None):
    """Capture the screen."""
    try:
        pg.screenshot(file_name, region=region)
    except Exception as e:
        logger.error(f"Failed to capture screen {file_name}: {e}")
