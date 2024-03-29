"""This module provides the ColumnAggregator abstract class."""

from abc import abstractmethod, ABC

from numpy import ndarray


class ColumnAggregator(ABC):
    """
    Reduce (aggregate) a series of data into a scalar value.
    """

    @abstractmethod
    def aggregate(self, column: ndarray):
        """
        When overridden in derived classes, reduce (aggregate) data in the given column into a
        scalar, and return that scalar.
        """
        raise NotImplementedError()
