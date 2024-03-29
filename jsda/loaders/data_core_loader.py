"""This module provides DataCoreLoader which loads data from DataCore."""

from data_core import GenericTabularData
from pandas import DataFrame

from jsda.loaders import DataLoader


class DataCoreLoader(DataLoader):
    """
    A DataLoader implementation that loads data from DataCore.
    """

    def __init__(self, **kwargs) -> None:
        self._kwargs = kwargs

    def load(self) -> DataFrame:
        return GenericTabularData(**self._kwargs).as_data_frame()
