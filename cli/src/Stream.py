from io import StringIO
import os


class Stream:
    def __init__(self):
        self.stream = StringIO()


class InputStream(Stream):
    def get_data(self):
        return self.stream.getvalue()


class OutputStream(Stream):
    def write(self, str):
        self.stream.write(str)

    def write_line(self, str):
        self.write(str)
        self.write(os.linesep)

    def convert_to_input_stream(self):
        input_stream = InputStream()
        input_stream.stream.write(self.stream.getvalue())
        return input_stream
