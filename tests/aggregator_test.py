import numpy as np

from jsda.aggregators.basic_statistics import Average, Max, Median, Min


def test_min():
    aggregator = Min()
    result = aggregator.aggregate(np.array([3, 2, 1]))
    assert result == 1


def test_max():
    aggregator = Max()
    result = aggregator.aggregate(np.array([1, 2, 3]))
    assert result == 3


def test_average():
    aggregator = Average()
    result = aggregator.aggregate(np.array([1, 2, 3]))
    assert result == 2


def test_median():
    aggregator = Median()
    result = aggregator.aggregate(np.array([1, 2, 3]))
    assert result == 2
