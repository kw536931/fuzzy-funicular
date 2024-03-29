# Design

The data aggregator loads a data table from some data source, and reduces each
column of the table into a scalar as the output. From this simple description,
we can already extract two core abstractions of the data aggregator: 1) the data
loader, and 2) the column aggregator. These two core abstractions are
represented by the two abstract base classes [`DataLoader`] and
[`ColumnAggregator`], respectively.

[`DataLoader`]: ../jsda/loaders/data_loader.py
[`ColumnAggregator`]: ../jsda/aggregators/column_aggregator.py

## `DataLoader`

The `DataLoader` abstract base class (ABC) represents a data loader that loads a
data table from some data source:

```python
from abc import abstractmethod, ABC
from pandas import DataFrame

class Loader(ABC):
    @abstractmethod
    def load(self) -> DataFrame:
        pass
```

By inheriting the `DataLoader` class from `abc.ABC`, we explicitly mark the
`DataLoader` class as an abstract base class. An abstract base class provides
an interface; typically they cannot be instantiated (i.e. you cannot create an
object of type `DataLoader` directly). Conceptually, abstract base classes are
similar to Java `interface`s or C++ abstract classes.

Note that we also decorate the `Loader.load` method with the `@abstractmethod`
decorator. By doing this, we explicitly mark that this method is abstract and
its implementation should be provided by subclasses.

### Some Object Oriented Design Philosophy

> [!TIP]
> You can skip this section if you're already familiar with object oriented
> programming.

Abstract base classes are one of the most common techniques in object oriented
programming (OOP). It effectively hides the implementation details of your
component away from its downstream users. Code that works on a data table really
doesn't care where the data table comes from; it just needs an interface to grab
the data and does its job, and that's the abstraction provided by `DataLoader`.
Furthermore, by providing downstream code with different implementations of
`DataLoader`, you can easily customize the data source your downstream users
actually depend. Your users were loading data from parquet files and suddenly
one day they want to load data from DataCore instead, you just provide them with
`DataCoreLoader` instead of `ParquetLoader` and the job is done. This idea is
so important in OOP that it is considered one of the 5 fundamental principles
in object oriented designs, namely "dependency inversion principle". The other
4 principles are:

- Single-responsibility principle;
- Open-closed principle;
- Liskov substitution principle, and
- Interface segregation principle.

Collectively, these 5 fundamental principles are called "SOLID" principles. You
can refer to its [wikipedia page](https://en.wikipedia.org/wiki/SOLID) for more
information.

### Implementations

To implement the interface provided by an abstract base class, we define classes
that derive from the abstract base class and override all the abstract methods
defined in the abstract base class. In this demo project, we provide 3
implementations of the `DataLoader` abstract base class: [`DataCoreLoader`],
[`ParquetLoader`], and `CsvLoader`. The last one is implemented in C++.

[`DataCoreLoader`]: ../jsda/loaders/data_core_loader.py
[`ParquetLoader`]: ../jsda/loaders/parquet_loader.py

Let's take `DataCoreLoader` as the example. It is defined like this:

```python
from data_core import GenericTabularData
from pandas import DataFrame

from jsda.loaders import DataLoader

class DataCoreLoader(DataLoader):
    def __init__(self, **kwargs) -> None:
        self._kwargs = kwargs

    def load(self) -> DataFrame:
        return GenericTabularData(**self._kwargs).as_data_frame()
```

The `DataCoreLoader` class derives from `DataLoader` and implements the `load`
method. This makes `DataCoreLoader` an implementation of `DataLoader`.

## `ColumnAggregator`

The `ColumnAggregator` is another abstract base class that models the interface
provided by the column aggregators. A column aggregator accepts an array of data
and reduces the data array into a scalar data. The `ColumnAggregator` class is
defined like the following:

```python
from abc import abstractmethod, ABC
from numpy import ndarray

class ColumnAggregator(ABC):
    @abstractmethod
    def aggregate(self, column: ndarray):
        pass
```

The `aggregate` abstract method takes an array of data and produces a scalar
value out of the data array.

This demo project also provides some implementations of `ColumnAggregator`,
most of which are defined in `jsda/aggregators/basic_statistics.py`. These
aggregators calculates some of the statistical metrics (e.g. min, max, average)
of the input data array.

## Extendability

It's also easy to extend the functionalities. If we want to support a new type
of data source, just add another implementation of `DataLoader`. Similarly, if
we want to support a new data aggregation algorithm, just add another
implementation of `ColumnAggregator`.
