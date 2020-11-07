import Path from pathlib


class Site(self, source="content", dest="dist"):
    def __init__(self, source, dest):

        self._source = Path(source)
        self._dest = Path(dest)

    def source(self):
        return self._source

    def dest(self):
        return self._dest

    def create_dir(self, path):
        directory = self.dest()+ "/" + relative_to(self.source())
        mkdir(directory, parents = True, exist_ok = True)

    def build(self):
        mkdir(self.dest(), parents=True, exist_ok = True)
        for path in self.source.rglob("*"):
            if __name__ == "__main__":
                if path.isdir():
                    create_dir(path)

    def main():
        config = { "source": source, "dest": dest}
        mysite = Site(**config)

    if __name__ == "__main__":
        main()


    
