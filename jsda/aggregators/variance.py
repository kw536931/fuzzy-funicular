from jsda.aggregators import ColumnAggregator
from jsda.jsda_cpp import CppVarianceAggregator


class Variance(ColumnAggregator):
    def __init__(self):
        super().__init__()
        self._inner = CppVarianceAggregator()

    def aggregate(self, column):
        return self._inner.aggregate(column)
