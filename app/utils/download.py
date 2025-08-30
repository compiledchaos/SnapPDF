import img2pdf
from app.utils.logger import get_logger
from pathlib import Path

logger = get_logger("download")


def download(captures_folder=Path("captures"), output_file=Path("output.pdf")):
    try:
        with open(output_file, "wb") as f:
            f.write(img2pdf.convert([str(p) for p in captures_folder.glob("*.png")]))
    except Exception as e:
        logger.error(f"Failed to download PDF: {e}")
    else:
        logger.info(f"Downloaded PDF to {output_file}")
