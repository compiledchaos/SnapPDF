from app.utils.screen_shot import capture_screen
from app.utils.auto_click import auto_click
from app.utils.logger import get_logger
import time
from pathlib import Path
import pyautogui as pg

logger = get_logger("start")


def start(
    num_clicks,
    click_method="Key",
    key="right",
    region=None,
    interval=1,
    output_folder="captures",
):
    logger.info("Starting SnapPDF")

    if region:
        x = region[0] + region[2] // 2
        y = region[1] + region[3] // 2
        pg.click(x=x, y=y)

    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True)
    for i in range(num_clicks):
        auto_click(click_method, key)
        capture_screen(output_folder / f"screenshot_{i+1}.png", region=region)
        time.sleep(interval)
    logger.info("Finished SnapPDF")
