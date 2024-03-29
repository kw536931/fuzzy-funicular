"""This module provides ParquetLoader which loads data from local parquet files."""

from pathlib import Path

from pandas import DataFrame
import pyarrow.parquet as pq

from jsda.loaders import DataLoader


class ParquetLoader(DataLoader):
    """
    A DataLoader implementation that loads tabular data from a local parquet file.
    """

    def __init__(self, file_path: Path):
        self._file_path = file_path

    def load(self) -> DataFrame:
        return pq.read_pandas(self._file_path)
