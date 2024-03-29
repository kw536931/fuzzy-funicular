"""This module provides the DataLoader abstract base class."""

from abc import abstractmethod, ABC
from pandas import DataFrame


class DataLoader(ABC):
    """
    Abstract base class for data loaders.

    Subclasses should implement the load method to load data.
    """

    @abstractmethod
    def load(self) -> DataFrame:
        """
        When overridden in derived classes, load data from data source as a pandas data frame.
        """
        raise NotImplementedError()
