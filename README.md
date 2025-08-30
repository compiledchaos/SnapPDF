# SnapPDF

A lightweight desktop tool to batch-capture screenshots of a selected screen region and save them as images, then combine them into a single PDF.

## Features
- Select an on-screen region to capture via a full-screen selector.
- Advance between pages with a key press (e.g., Right Arrow) or mouse click.
- Adjustable interval between captures.
- Images saved under `C:/Users/<your-user>/SnapPDF/captures/`.
- PDF export to `C:/Users/<your-user>/SnapPDF/output.pdf`.

## Requirements
- Windows 10/11
- Python 3.11+
- Dependencies in `requirements.txt`:
  - PySide6, pyautogui, keyboard, img2pdf, pillow, pytest (for tests)

Install dependencies:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run
Start the app from the project root:
```powershell
python -m app.core.core
```

On first run, the app creates a persistent folder at:
```
C:/Users/<your-user>/SnapPDF/
```
Subfolders/files:
- `captures/` — all screenshots
- `output.pdf` — exported PDF

## Usage
1. Enter the number of pages to capture and the interval (seconds).
2. Choose advance method: `Key` (default) or `Click`.
   - For `Key`, specify a key like `right`, `pagedown`, etc.
   - For `Click`, specify a mouse button like `left`, `right`, etc.
3. Click Start.
4. Use the on-screen selector to draw the capture region.
5. The app will:
   - Focus-click the center of the selected region (once).
   - Repeatedly advance and capture the region for the specified number of pages.
6. Click Download PDF to generate `output.pdf` from the captured images.

## Notes on display scaling (DPI)
- The region selector runs in logical pixels; the app converts to physical pixels to align with `pyautogui` so captures should match your selection, even on high-DPI displays.
- If captures appear offset on multi-monitor/mixed-DPI setups, please report your scaling settings so we can fine-tune detection.

## Tests
Run tests with pytest from the project root:
```powershell
python -m pytest -q
```
Included tests:
- `tests/test_start.py` — verifies capture loop, initial focus-click, and parameter flow.
- `tests/test_download.py` — validates PDF generation with mocked conversion.

## Logging
Logs are written to `logs/snappdf.log` during development runs. Review this file for diagnostics if something goes wrong.

## Project structure
```
app/
  core/core.py            # App entry point
  ui/                     # Qt UI and dialogs
  utils/                  # Helpers: paths, logging, capture, etc.
assets/                   # Icons and static assets
captures/                 # (dev) may be ignored; runtime uses user folder
```

## Troubleshooting
- If hotkeys or clicks don’t work, ensure the target window is focused. The app performs an initial click in the region center to help.
- If no images are captured, check `logs/snappdf.log` for errors and verify permissions.
- If PDF is empty, confirm `.png` files exist in the `captures/` folder under your user SnapPDF directory.
