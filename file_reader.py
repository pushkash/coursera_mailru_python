class FileReader:
    """Класс FileReader помогает читать файлы"""

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except IOError:
            return ""


fr = FileReader("oop.py")

print(fr.read())
