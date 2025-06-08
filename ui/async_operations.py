import json
import yaml
import xml.etree.ElementTree as ET
from PyQt5.QtCore import QThread, pyqtSignal


class AsyncFileHandler(QThread):
    finished = pyqtSignal(object)

    def __init__(self, file_path, file_format, operation, data=None):
        super().__init__()
        self.file_path = file_path
        self.format = file_format
        self.operation = operation
        self.data = data

    def run(self):
        try:
            if self.operation == "load":
                result = self._load_file()
            elif self.operation == "save":
                result = self._save_file()
            self.finished.emit(result)
        except Exception as e:
            self.finished.emit(f"Error: {e}")

    def _load_file(self):
        with open(self.file_path, "r") as file:
            if self.format == "json":
                return json.load(file)
            elif self.format == "yaml":
                return yaml.safe_load(file)
            elif self.format == "xml":
                return ET.parse(file).getroot()

    def _save_file(self):
        with open(self.file_path, "w") as file:
            if self.format == "json":
                json.dump(self.data, file, indent=4)
            elif self.format == "yaml":
                yaml.dump(self.data, file)
            elif self.format == "xml":
                root = ET.Element("data")
                for key, value in self.data.items():
                    ET.SubElement(root, key).text = str(value)
                ET.ElementTree(root).write(file)
        return f"File saved: {self.file_path}"