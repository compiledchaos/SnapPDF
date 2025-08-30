import img2pdf
from app.utils.logger import get_logger
from pathlib import Path
from app.utils.paths import captures_dir, output_pdf_path, ensure_runtime_dirs

logger = get_logger("download")


def download(captures_folder: Path | None = None, output_file: Path | None = None):
    try:
        ensure_runtime_dirs()
        captures_folder = captures_folder or captures_dir()
        output_file = output_file or output_pdf_path()
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "wb") as f:
            f.write(img2pdf.convert([str(p) for p in captures_folder.glob("*.png")]))
    except Exception as e:
        logger.error(f"Failed to download PDF: {e}")
    else:
        logger.info(f"Downloaded PDF to {output_file}")
