# Development

This document gives you instructions on common development tasks including:

- How to setup the development environment for this project;
- How to build and run the project;
- How to ensure your code quality with code formatters and linters;
- How to do version control properly.

## Getting Started

Clone this project to local:

```bash
git clone git@github.com:sm813471/python-project-demo.git
cd python-project-demo
```

Then execute the following command to install a git commit hook that checks
your code quality automatically when committing changes:

```bash
cp scripts/pre-commit .git/hooks
```

### Setup for vscode

For vscode users, we recommend you use the [devcontainer] feature for setting up
your development environment. We have already prepared the devcontainer
configurations. Please make sure that you have the `Dev Containers` extension
installed. The extension's ID is `ms-vscode-remote.remote-containers`.

After opening the `python-project-demo` directory in vscode, all you need to do
is instructing vscode to reopen the directory in devcontainer. To do this,
press `Ctrl + Shift + P` and execute the following command: `Dev Containers:
Reopen in Container` and it's done.

[devcontainer]: https://code.visualstudio.com/docs/devcontainers/containers

![open in devcontainers](https://code.visualstudio.com/assets/docs/devcontainers/create-dev-container/dev-containers-reopen.png)

### Setup for PyCharm

> TODO.

## Dependencies

### Python Dependencies Management

This Python project uses [`pyproject.toml`] to manage its dependencies. This
file is a text file in [TOML] format that describes the Python project.

[`pyproject.toml`]: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
[TOML]: https://toml.io/en/

The project's dependencies are listed in the `pyproject.toml` file. There are 2
kinds of dependencies:

1. Runtime dependencies. These dependencies are those Python packages that are
   required when this package runs. Typically these dependencies are `import`-ed
   into somewhere in this package. Runtime dependencies are listed in the
   `project.dependencies` field.
2. Build dependencies. These dependencies are those Python packages that are
   required when packaging the project. Build dependencies are listed in the
   `build-system.requires` field.

Unfortunately, currently `pip` cannot automatically install the runtime
dependencies listed. You have to manually install those dependencies through
`pip` commands:

```bash
pip3 install numpy pandas pyarrow=="8.0.1"
```

### C++ Dependencies Management

> TODO.

## Build

> [!NOTE]
> This section only provides information about the C++ extension in the
> project. If you're only interested in the Python part, you can skip this
> section.

This section gives you instructions on how to build the C++ extension contained
in this project. At the beginning, we assume that the current working directory
is the project's root directory.

Before building, please make sure that all necessary build tools are installed
via the following command:

```bash
sudo apt install cmake g++ ninja-build
```

Create a build directory:

```bash
mkdir build-cpp
cd build-cpp
```

Build with CMake:

```bash
cmake -G Ninja -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
```

If you want to build a release version, replace `-DCMAKE_BUILD_TYPE=Debug` with
`-DCMAKE_BUILD_TYPE=Release`. There are other possible CMake options you can
specify to further customize the build output. For more information on the usage
of CMake, please refer to [CMake official documentation].

[CMake official documentation]: https://cmake.org/cmake/help/latest/

After building the extension, add a soft link inside the `jsda` subdirectory so
the `jsda` package can import it properly:

```
cd ../jsda
ln -s ../build-cpp/jsda_cpp/jsda_cpp.cpython-310-x86_64-linux-gnu.so
```

## Run `jsda` CLI

This project provides a simple CLI for the data aggregator. The entrypoint file
is `main.py`. Since this project contains a C++ extension, you need to
[build](#build) the C++ extension before you run the CLI tool.

To run the CLI tool, run the following command:

```bash
python3 main.py
```

You may pass `--help` to `main.py` for usage information.

## `clangd`

> [!NOTE]
> This section is only relevant with C++ extension development. If you are only
> interested in developing a pure Python project, you can skip this section.

[`clangd`] is a C++ language server. It provides functionalities such as C++
code completion, refactoring, jump to definition, etc. Using `clangd` can
greatly improve your C++ development experiences.

[`clangd`]: https://clangd.llvm.org/

To install `clangd` in your system, run the following command:

```bash
sudo apt install clangd
```

You need to prepare a configuration file for `clangd` to make it work properly
for you. The configuration file tells `clangd` crucial information such as
header file locations so that `clangd` can understand your source code. We
cannot prepare this file for you in advance because the content of this file
depends on the exact development environment and configurations.

Luckily, CMake can generate this configuration file for you. Enter the build
directory and run the following command:

```bash
cd build-cpp
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ..
```

CMake will generate a file named `compile_commands.json` in the build directory.
Create a symbolic link to this file in the project's root directory:

```bash
cd ..
ln -s build-cpp/compile_commands.json
```

And now `clangd` should just work.

## Code Formatters and Linters

In JQ, we use verified code formatters and linters to guard our software
quality. In your project, you should take good use of these tools as well.

### Code Formatters

Code formatters are tools that automatically adjust your code style to make it
consistent with the company's standard.

For Python code, we use [`autopep8`] as the code format tool. You can install
`autopep8` via `pip`:

[`autopep8`]: https://pypi.org/project/autopep8

```bash
pip3 install autopep8
```

To format a specific source code file, run the following command:

```bash
autopep8 -iaa /path/to/your/source/file.py
```

If you are using vscode, you may also use vscode's format file functionality to
format the source code file.

For C++ code, we use [`clang-format`] as the code format tool. We have also
prepared its configuration for you in the `.clang-format` file. You can install
`clang-format` by running the following command:

[`clang-format`]: https://clang.llvm.org/docs/ClangFormat.html

```bash
sudo apt install clang-format
```

To format a specific source code file, run the following command:

```bash
clang-format /path/to/your/source/file.cpp
```

If you are using vscode, you may also use vscode's format file functionality to
format the source code file.

### Linters

Linters are static code checkers that can identify potential problems and bugs
in your code. A properly configured linter can help you discover quite a lot
problems in your code early before they cause real problems.

For Python code, we use [`pylint`] as the linter. We use the default set of lint
rules bundled in `pylint` so we don't have to prepare any configuration files.
You can install `pylint` via `pip`:

[`pylint`]: https://pylint.readthedocs.io/en/stable/

```bash
pip3 install pylint
```

To run `pylint` to check a specific source code file, run the following command:

```bash
pylint /path/to/your/source/file.py
```

For C++ code, we use [`clang-tidy`] as the linter. We have prepared its
configuration file for you in the `.clang-tidy` file. You can install
`clang-tidy` by running the following command:

[`clang-tidy`]: https://clang.llvm.org/extra/clang-tidy/

```bash
sudo apt install clang-tidy
```

To run the C++ linter on a specific C++ source code file, run the following
command:

```bash
clang-tidy /path/to/your/source/file.cpp
```

Note that `clangd` has built-in support for `clang-tidy` checks. If you are
using vscode, `clangd` will give you warnings as you code. Typically you don't
have to run `clang-tidy` command yourself.

## Tests

This project is a Python/C++ hybrid project. We have different test tools and
workflows in Python world and C++ world.

### Python Tests

In JQ, we use [`pytest`] to organize and run Python unit tests. You can install
`pytest` via `pip`:

[`pytest`]: https://docs.pytest.org/en

```bash
pip3 install pytest
```

By convention, all python unit tests are kept under the `tests` subdirectory.
Each `*_test.py` file or `test_*.py` file under this directory are test files.
Each function defined in a test file is a unit test.

To run all Python unit tests, run the following command:

```bash
python3 -m pytest
```

> [!IMPORTANT]
> You must run `pytest` with the command shown above. Do not execute `pytest`
> directly or you may get import errors.

### C++ Tests

In JQ, we use [`googletest`] to organize and run our C++ unit tests. By
convention, all source code files of C++ unit tests are kept under
`jsda_cpp/tests` subdirectory. These source files are also listed in the
`jsda_cpp/tests/CMakeLists.txt` file.

[`googletest`]: https://google.github.io/googletest/primer.html

You need to [build](#build) the C++ extension before you can run the unit tests.
To run all C++ unit tests, enter the build directory and run `ctest`:

```bash
cd build-cpp
ctest
```

## Version Control

We use git to do version control. We use multiple branches to track the
different development progress and release versions. In short:

For a complete guide on how we do version control with git, you can follow
[Manage and release a Python Project].

[Manage and release a Python Project]: https://v9kg4fi819.feishu.cn/docx/Vza3d9ogXoWBB3xLjH2cxTdHnug?from=from_copylink
