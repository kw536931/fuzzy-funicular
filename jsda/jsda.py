"""
This module provides the JSDA class, which is the central class of the jsda project.
"""

from typing import Dict, Union

from jsda.loaders import DataLoader
from jsda.aggregators import ColumnAggregator


class JSDA:
    """
    Jiaqi Simple Data Aggregator
    """

    def __init__(self,
                 data_loader: DataLoader,
                 aggregators: Union[ColumnAggregator, Dict[str, ColumnAggregator]],
                 ) -> None:
        df = data_loader.load()

        self._aggregate_result = {}
        for column_name, column_series in df.items():
            # Get the column aggregator corresponding to the current series.
            aggr = aggregators
            if isinstance(aggr, dict):
                aggr = aggr.get(column_name, None)
            if aggr is None:
                continue

            column_aggregate_result = aggr.aggregate(column_series.to_numpy())
            self._aggregate_result[column_name] = column_aggregate_result

    @property
    def aggregate_result(self) -> dict:
        """
        Get the aggregation result.
        """

        return self._aggregate_result
