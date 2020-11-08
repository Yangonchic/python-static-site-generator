from typing import List
import shutil

from pathlib import Path

class Parser:
    def copy(self, path, source, dest):
        copy2(path, self.dest/path.relative_to(self.source))

    extensions = []
    pass

    def valid_extension(self, extension):
        return extension in Parser.extensions

    def parse(self, path, source, dest):
        raise NotImplementedError

    def read(self, path):
        with open(path) as reader:
            return reader.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            write(content)

class ResourceParser(Parser):
    extensions = ["jpg", ".png", ".gif", ".css", ".html"]

    def parse(self):
        super.copy(path, source, dest)
