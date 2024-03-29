cmake_minimum_required(VERSION 3.22)
project(jsda)

if (NOT PROJECT_IS_TOP_LEVEL)
    message(FATAL_ERROR "${PROJECT_NAME} can only be built as the root project.")
endif ()

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake/modules)

include(CTest)
include(cmake/AddDeps.cmake)

add_subdirectory(jsda_cpp)
