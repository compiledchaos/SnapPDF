from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.utils.paths import ensure_runtime_dirs

if __name__ == "__main__":
    ensure_runtime_dirs()
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()