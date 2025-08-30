"""Main application window and user interactions.

Handles area selection, screenshotting, auto-clicking, and start flow coordination.
"""

from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QGuiApplication
from PySide6.QtCore import QEventLoop
from .main_window_ui import Ui_MainWindow
from app.utils.logger import get_logger
from app.utils.paths import asset_path
from app.utils.start import start
from app.utils.download import download
from .dialogs import ScreenSelector

logger = get_logger("main_window")


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window class wiring UI to actions."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pageInput.textChanged.connect(self.update_ui)
        self.intervalInput.textChanged.connect(self.update_ui)
        self.advanceKeyInput.textChanged.connect(self.update_ui)
        self.advanceMethod.currentIndexChanged.connect(self.update_ui)

        self.pushButton_4.clicked.connect(self.start)
        self.pushButton_3.clicked.connect(self.download)

        # Set window icon from assets if available
        self.setup_icon()

    def select_region(self):
        """Select the region to capture."""
        selector = ScreenSelector()
        loop = QEventLoop()
        region_tuple = {"val": None}

        def on_selection_complete(rect):
            # Convert QRect (logical pixels) to physical pixels for pyautogui
            screen = QGuiApplication.primaryScreen()
            dpr = screen.devicePixelRatio() if screen else 1.0
            x = int(rect.x() * dpr)
            y = int(rect.y() * dpr)
            w = int(rect.width() * dpr)
            h = int(rect.height() * dpr)
            region_tuple["val"] = (x, y, w, h)
            loop.quit()

        selector.selection_complete.connect(on_selection_complete)
        selector.show()
        # Block until selection is made
        loop.exec()
        return region_tuple["val"]

    def start(self):
        """Start the screenshotting and auto-clicking process."""
        start(
            int(self.pageInput.text()),
            self.advanceMethod.currentText(),
            self.advanceKeyInput.text(),
            self.select_region(),
            int(self.intervalInput.text()),
        )

    def download(self):
        """Download the screenshots to a PDF."""
        download()

    def update_ui(self):
        """Enable start button only if all inputs are valid."""
        self.pushButton_4.setEnabled(
            bool(
                self.pageInput.text()
                and self.intervalInput.text()
                and self.advanceKeyInput.text()
            )
        )

    def setup_icon(self):
        """Set the window icon from assets."""
        # Try to find and set the icon from assets
        icon_path = None
        for name in ("book.ico", "book.png"):
            candidate = asset_path(name)
            if candidate.exists():
                icon_path = candidate
                break
        if icon_path is not None and icon_path.exists():
            try:
                self.setWindowIcon(QIcon(str(icon_path)))
                logger.info(f"Window icon set: {icon_path}")
            except Exception as e:
                logger.warning(f"Failed to set window icon from {icon_path}: {e}")
        else:
            logger.debug("No book icon found in assets; using default icon")
