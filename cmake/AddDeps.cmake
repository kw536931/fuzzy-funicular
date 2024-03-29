include_guard(GLOBAL)
include(FetchContent)

find_package(Python3 3.10
    REQUIRED
    COMPONENTS Interpreter Development.Module
)
find_package(pyarrow REQUIRED)

set(jsda_deps
    pybind11
)

FetchContent_Declare(
    pybind11
    URL https://github.com/pybind/pybind11/archive/refs/tags/v2.11.1.tar.gz
    URL_HASH SHA256=d475978da0cdc2d43b73f30910786759d593a9d8ee05b1b6846d1eb16c6d2e0c
)

if (BUILD_TESTING)
    FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.tar.gz
    )
    list(APPEND jsda_deps googletest)
endif ()

FetchContent_MakeAvailable(${jsda_deps})
