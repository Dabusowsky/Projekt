import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QPushButton, QFileDialog, QLabel, QComboBox
)
from PyQt5.QtCore import QThread, pyqtSignal
from async_operations import AsyncFileHandler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Processor (Async)")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Select a file and operation:")
        self.combo_format = QComboBox()
        self.combo_format.addItems(["JSON", "YAML", "XML"])
        self.btn_open = QPushButton("Open File")
        self.btn_save = QPushButton("Save File")
        self.status_label = QLabel("Ready.")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combo_format)
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_save)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.btn_open.clicked.connect(self.open_file)
        self.btn_save.clicked.connect(self.save_file)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_path:
            self.status_label.setText("Loading...")
            format_type = self.combo_format.currentText().lower()
            self.worker = AsyncFileHandler(file_path, format_type, "load")
            self.worker.finished.connect(self.on_loaded)
            self.worker.start()

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File")
        if file_path:
            self.status_label.setText("Saving...")
            format_type = self.combo_format.currentText().lower()
            data = {"sample_data": "Test"}  # Przykładowe dane
            self.worker = AsyncFileHandler(file_path, format_type, "save", data)
            self.worker.finished.connect(self.on_saved)
            self.worker.start()

    def on_loaded(self, result):
        self.status_label.setText(f"Loaded: {result}")

    def on_saved(self, result):
        self.status_label.setText(f"Saved: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())