from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import json
from pathlib import Path

from jsda import JSDA
from jsda.loaders.parquet_loader import ParquetLoader
from jsda.loaders.data_core_loader import DataCoreLoader
from jsda.aggregators.basic_statistics import Average, Max, Median, Min


if __name__ != "__main__":
    print("This module can only be used as the main script.")
    exit(1)


def parse_args():
    parser = ArgumentParser(description="Jiaqi Simple Data Aggregator",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--config", default="config.json", metavar="CONFIG_FILE", type=Path,
                        help="path to the configuration file")
    return parser.parse_args()


args = parse_args()
with open(args.config, "r", encoding="utf-8") as fp:
    config = json.load(fp)


def create_data_core_loader() -> DataCoreLoader:
    data_core_params = config["loader"]["params"]
    return DataCoreLoader(**data_core_params)


def create_parquet_loader() -> ParquetLoader:
    file_path = Path(config["loader"]["path"])
    return ParquetLoader(file_path)


def create_data_loader():
    factories = {
        "data_core": create_data_core_loader,
        "parquet": create_parquet_loader,
    }
    return factories[config["loader"]["type"]]()


def create_aggregator():
    factories = {
        "min": Min,
        "max": Max,
        "average": Average,
        "median": Median,
    }
    return factories[config["aggregator"]["type"]]


loader = create_data_loader()
aggregator = create_aggregator()
jsda = JSDA(loader, aggregator)

for k, v in jsda.aggregate_result.items():
    print(f"{k} = {v}")
