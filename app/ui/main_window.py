"""Main application window and user interactions.

Handles area selection, screenshotting, auto-clicking, and start flow coordination.
"""

from PySide6.QtWidgets import QMainWindow, QFrame, QLabel, QMessageBox
from PySide6.QtGui import QIcon, QGuiApplication, QDesktopServices
from PySide6.QtCore import QEventLoop, QUrl, Qt
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

        self.support_clicked = False

        self.ad_label = QLabel(self)
        self.ad_label.setText("CLICK HERE before starting!")
        self.ad_label.setAlignment(Qt.AlignCenter)
        self.ad_label.setStyleSheet(
            "background-color: #ffeb3b; color: #000; font-weight: 700; padding: 12px; border-radius: 6px;"
        )
        self.ad_label.setCursor(Qt.PointingHandCursor)
        self.ad_label.mousePressEvent = lambda e: self.on_support_clicked()
        # Place the support banner just above the Start button (before spacer)
        idx = self.layout.indexOf(self.pushButton_4)
        if idx == -1:
            self.layout.addWidget(self.ad_label)
        else:
            self.layout.insertWidget(idx, self.ad_label)

        self.pageInput.textChanged.connect(self.update_ui)
        self.intervalInput.textChanged.connect(self.update_ui)
        self.advanceKeyInput.textChanged.connect(self.update_ui)
        self.advanceMethod.currentIndexChanged.connect(self.update_ui)

        self.pushButton_4.clicked.connect(self.start)
        self.pushButton_3.clicked.connect(self.download)

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
        if not self.support_clicked:
            QMessageBox.information(
                self,
                "Support Required",
                "Please click the support banner before starting.",
            )
            return
        start(
            int(self.pageInput.text()),
            self.advanceMethod.currentText(),
            self.advanceKeyInput.text(),
            self.select_region(),
            int(self.intervalInput.text()),
        )
        self.support_clicked = False
        self.update_ui()

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
                and self.support_clicked
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

    def on_support_clicked(self):
        QDesktopServices.openUrl(
            QUrl(
                "https://www.effectivegatecpm.com/akz0b236?key=5c82455032830766db62a6c2b7ed833f"
            )
        )
        self.support_clicked = True
        self.update_ui()
