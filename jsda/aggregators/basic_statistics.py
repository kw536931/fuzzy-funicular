"""
This module provides a collection of column aggregators that yield basic statistics of the input
data columns.
"""

import numpy as np

from jsda.aggregators import ColumnAggregator


class Min(ColumnAggregator):
    """
    A ColumnAggregator implementation that returns the minimum value in a data column as its
    aggregated output.
    """

    def aggregate(self, column: np.ndarray):
        return column.min()


class Max(ColumnAggregator):
    """
    A ColumnAggregator implementation that returns the maximum value in a data column as its
    aggregated output.
    """

    def aggregate(self, column: np.ndarray):
        return column.max()


class Average(ColumnAggregator):
    """
    A ColumnAggregator implementation that returns the average value in a data column as its
    aggregated output.
    """

    def aggregate(self, column: np.ndarray):
        return np.average(column)


class Median(ColumnAggregator):
    """
    A ColumnAggregator implementation that returns the median value in a data column as its
    aggregated output.
    """

    def aggregate(self, column: np.ndarray):
        return np.median(column)
