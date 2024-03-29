from jsda.loaders import DataLoader
from jsda.jsda_cpp import CppCsvLoader


class CsvLoader(DataLoader):
    def __init__(self, path):
        super().__init__()
        self._inner = CppCsvLoader(path)

    def load(self):
        return self._inner.load()
