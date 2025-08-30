"""Selection overlay dialog to choose a screen region.

Renders a dimmed desktop snapshot and a transparent selection rectangle.
"""

from PySide6.QtCore import Qt, QRect, QPoint, Signal
from PySide6.QtGui import QPainter, QPen, QColor, QGuiApplication
from PySide6.QtWidgets import QWidget


class ScreenSelector(QWidget):
    # Define a signal that will be emitted when selection is complete
    selection_complete = Signal(object)  # Will emit the QRect

    def __init__(self):
        """Initialize a fullscreen overlay for region selection."""
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setWindowState(Qt.WindowFullScreen)
        # Translucent background is supported on most Win10+ systems, but to avoid black
        # fallback we draw the captured desktop ourselves.
        self.setCursor(Qt.CrossCursor)
        self.start = QPoint()
        self.end = QPoint()
        self.selection = None
        # Capture current desktop image to use as background while selecting
        try:
            screen = QGuiApplication.primaryScreen()
            self._bg = screen.grabWindow(0) if screen else None
        except Exception:
            self._bg = None

    def mousePressEvent(self, event):
        """Start the selection at current mouse position."""
        self.start = event.pos()
        self.end = self.start
        self.update()

    def mouseMoveEvent(self, event):
        """Resize selection as the mouse moves."""
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        """Finalize selection and emit rectangle."""
        self.end = event.pos()
        self.selection = QRect(self.start, self.end).normalized()
        # Emit the signal with the selection before closing
        self.close()  # Close selector after selection
        self.selection_complete.emit(self.selection)

    def paintEvent(self, event):
        """Paint background dim and selection cutout + border."""
        painter = QPainter(self)
        rect = QRect(self.start, self.end).normalized()

        # Draw captured desktop if available; otherwise leave as-is
        if self._bg is not None:
            painter.drawPixmap(0, 0, self._bg)

        # Dim the screen with a translucent overlay
        painter.fillRect(self.rect(), QColor(0, 0, 0, 120))

        # Clear the selection area to reveal the desktop
        painter.setCompositionMode(QPainter.CompositionMode_Clear)
        painter.fillRect(rect, Qt.transparent)

        # Draw selection border on top
        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.setBrush(Qt.transparent)
        painter.drawRect(rect)
