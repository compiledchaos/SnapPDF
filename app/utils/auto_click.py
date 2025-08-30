import pyautogui as pg
from app.utils.logger import get_logger

logger = get_logger("auto_click")


def auto_click(click_method="Key", key="right"):
    if click_method == "Key":
        try:
            pg.press(key)
        except Exception as e:
            logger.error(f"Failed to press key {key}: {e}")
    elif click_method == "Click":
        try:
            pg.click(button=key)
        except Exception as e:
            logger.error(f"Failed to click mouse button {key}: {e}")
    else:
        logger.error(f"Invalid click method: {click_method}")
