"""Generated-like UI wiring for the main window layout and widgets."""

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QPushButton,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QCheckBox,
    QLabel,
)
from PySide6.QtGui import QStandardItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 300)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Frame
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(0, 0, 250, 300)

        # Use vertical layout inside the frame
        self.layout = QVBoxLayout(self.frame)
        self.layout.setContentsMargins(20, 20, 20, 0)
        self.layout.setSpacing(20)

        # Page input
        self.pageInput = QLineEdit(self.frame)
        self.pageInput.setPlaceholderText("Please enter number of pages")
        self.pageInput.setAlignment(Qt.AlignCenter)

        # Interval input
        self.intervalInput = QLineEdit(self.frame)
        self.intervalInput.setPlaceholderText("Please enter interval")
        self.intervalInput.setAlignment(Qt.AlignCenter)

        # --- Advance controls
        self.advanceMethod = QComboBox(self.frame)
        self.advanceMethod.model().clear()

        # Add Click option
        click_item = QStandardItem("Click")
        click_item.setTextAlignment(Qt.AlignCenter)
        self.advanceMethod.model().appendRow(click_item)

        # Add Key option
        key_item = QStandardItem("Key")
        key_item.setTextAlignment(Qt.AlignCenter)
        self.advanceMethod.model().appendRow(key_item)

        # Add None option
        none_item = QStandardItem("None")
        none_item.setTextAlignment(Qt.AlignCenter)
        self.advanceMethod.model().appendRow(none_item)
        self.advanceMethod.setCurrentIndex(1)  # Click by default

        # Advance key input
        self.advanceKeyInput = QLineEdit(self.frame)
        self.advanceKeyInput.setPlaceholderText("Advance key (e.g., right, pagedown)")
        self.advanceKeyInput.setAlignment(Qt.AlignCenter)
        self.advanceKeyInput.setText("right")

        # Download button
        self.pushButton_3 = QPushButton("Download PDF", self.frame)

        # Start button
        self.pushButton_4 = QPushButton("Start", self.frame)
        self.pushButton_4.setEnabled(False)

        # Spacer to push things towards center
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Add widgets to layout
        self.layout.addWidget(self.pageInput)
        self.layout.addWidget(self.intervalInput)
        self.layout.addWidget(self.advanceMethod)
        self.layout.addWidget(self.advanceKeyInput)
        self.layout.addWidget(self.pushButton_3)
        self.layout.addWidget(self.pushButton_4)
        self.layout.addItem(spacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "SnapPDF", None)
        )
