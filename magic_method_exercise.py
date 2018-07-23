import os
import tempfile

class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def __str__(self):
        return self.filepath

    def __add__(self, second_file):
        first_content = self.__getContent(self.filepath)
        second_content = self.__getContent(second_file.filepath)
        tmp_file_path = os.path.join(tempfile.gettempdir(), "test.txt")
        tmp_file = File(tmp_file_path)

        tmp_file.write(first_content + second_content)

        return tmp_file

    def __iter__(self):
        with open(self.filepath) as f:
            self.iterator = f.readlines()
            return iter(self.iterator)
        # return iter(self.filepath)

    def __next__(self):
        try:
            return next(self.iterator)
        except:
            raise StopIteration

    def write(self, content):
        with open(self.filepath, "w") as f:
            f.write(content)

    def read(self):
        with open(self.filepath) as f:
            return f.read()

    def __getContent(self, file):
        content = ""
        with open(file) as f:
            content = f.read()
        return content


# object_1 = File("test_1.txt")

# object_2 = File("test_2.txt")

# object_1.write("Hello there")

# object_2.write("Oh hi, Mark!")

# new_obj = object_1 + object_2

# print(type(new_obj))
