# Project Structure

This demo project is a hybrid project that uses both Python and C++. If you're
only interested in the Python part, just ignore the C++ part.

The following diagram gives this project's file structure. Each entry in the
file structure is prefixed by either of `[py]`, or `[hybrid]`. Entries with the
`[hybrid]` prefix should only be present if the project is a Python/C++ hybrid
project. If you are only interested in creating a pure Python project, just
focus on those entries with the `[py]` prefix.

<details>
<summary>Project structure of this demo project</summary>

```
├── [py] .devcontainer
│   ├── [py] devcontainer.json
│   └── [py] Dockerfile
│
├── [hybrid] cmake
│   ├── [hybrid] modules
│   │   └── [hybrid] Findpyarrow.cmake
│   │
│   └── [hybrid] AddDeps.cmake
│
├── [py] docs
│   └── [py] **/*.md
│
├── [py] jsda
│   ├── [py] __init__.py
│   ├── [py] jsda.py
│   │
│   ├── [py] aggregators
│   │   ├── [py] __init.py
│   │   ├── [py] basic_statistics.py
│   │   ├── [py] column_aggregator.py
│   │   └── [hybrid] variance.py
│   │
│   └── [py] loaders
│       ├── [py] __init.py
│       ├── [hybrid] csv_loader.py
│       ├── [py] data_core_loader.py
│       ├── [py] data_loader.py
│       └── [py] parquet_loader.py
│
├── [hybrid] jsda_cpp
│   ├── [hybrid] include
│   │   └── [hybrid] jsda
│   │       ├── [hybrid] Aggregators.hpp
│   │       └── [hybrid] Loaders.hpp
│   │
│   ├── [hybrid] src
│   │   ├── [hybrid] bindings
│   │   │   └── [hybrid] Module.cpp
│   │   │
│   │   ├── [hybrid] CsvLoader.cpp
│   │   └── [hybrid] VarianceAggregator.cpp
│   │
│   ├── [hybrid] tests
│   │   ├── [hybrid] CMakeLists.txt
│   │   └── [hybrid] VarianceAggregator.cpp
│   │
│   ├── [hybrid] .gitignore
│   └── [hybrid] CMakeLists.txt
│
├── [py] scripts
│   ├── [hybrid] git-clang-format.py
│   ├── [hybrid] pre-commit
│   └── [py] **/*.*
│
├── [py] tests
│   ├── [py] aggregator_test.py
│   └── [hybrid] variance_aggregator_test.py
│
├── [py] .gitignore
├── [hybrid] CMakeLists.txt
├── [py] main.py
├── [py] pyproject.toml
├── [py] README.md
└── [hybrid] setup.py
```

</details>

In the following subsections, we will give brief introductions on each of the
project root's subdirectories, and some of the important files in each
subdirectory.

## `.devcontainer`

This directory contains [devcontainer] configurations. Devcontainer is a vscode
feature that allows you to develop your project in a reproducible docker
container that contains all the necessary dependencies and environments
required. For more information, please refer to the official documentation.

[devcontainer]: https://code.visualstudio.com/docs/devcontainers/containers

## `cmake`

This directory contains CMake scripts for the C++ part of the project. The
`AddDeps.cmake` script in this directory configures the dependencies required to
build the C++ extension.

## `docs`

This directory contains any additional documents you want to be included in your
project. It may be missing if your project don't include any additional
documents.

## `jsda`

This is the directory of the `jsda` Python package. It's recommended that you
organize the core functionalities of your project into a standalone package so
it can be easily tested and distributed.

## `jsda_cpp`

This is the directory that contains the C++ source files of the hybrid project.
The structure of this subdirectory follows the convention adopted by the C++
community. All public header files reside in the `include/jsda_cpp`
subdirectory, and all other source files reside in the `src` directory. The
`tests` subdirectory contains C++ unit tests.

## `scripts`

This directory contains script files necessary for the project. It may be
missing if your project does not have any additional scripts.

## `tests`

This directory contains Python unit tests.
