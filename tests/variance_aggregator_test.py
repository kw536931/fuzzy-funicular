import math
import numpy as np

from jsda.aggregators.variance import Variance


def test_variance():
    aggregator = Variance()

    result = aggregator.aggregate(np.array([1, 2, 3, 4, 5]))
    assert abs(result - 2.0) <= 1e-8

    result = aggregator.aggregate(np.array([]))
    assert math.isnan(result)
