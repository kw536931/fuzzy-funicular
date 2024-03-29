# This CMake module finds the pyarrow installation in the current environment. It will set the following output
# variables in the calling scope:
#
# - pyarrow_FOUND: A boolean value indicating whether pyarrow is found.
#
# If a pyarrow installation is found, the following variables will be further set:
#
# - pyarrow_INCLUDE_DIR: Path to the pyarrow include directories.
# - pyarrow_LIBS_DIR: Path to the pyarrow library directories.
# - pyarrow_VERSION: Version of pyarrow found.
# - pyarrow_SOVER: Version of pyarrow shared libraries.
#
# Besides, the following IMPORTED library target will be added if a pyarrow installation is found:
#
# - arrow
# - arrow_python
# - parquet

include_guard(GLOBAL)

function (get_pyarrow_info pyarrow_expr output_variable)
    execute_process(
        COMMAND python3 -c "import pyarrow; print(${pyarrow_expr}, end='')"
        OUTPUT_VARIABLE pyarrow_output
        RESULT_VARIABLE pyarrow_status
    )

    if (NOT pyarrow_status EQUAL 0)
        if (NOT pyarrow_FIND_QUIETLY)
            message(WARNING "Failed to get ${output_variable}. Is pyarrow properly installed?")
        endif ()
        set(${output_variable} "" PARENT_SCOPE)
        return()
    endif ()

    string(STRIP "${pyarrow_output}" pyarrow_output)
    set(${output_variable} ${pyarrow_output} PARENT_SCOPE)
endfunction ()

get_pyarrow_info(
    "pyarrow.cpp_version"
    pyarrow_VERSION
)
get_pyarrow_info(
    "pyarrow.get_include()"
    pyarrow_INCLUDE_DIR
)
get_pyarrow_info(
    "pyarrow.get_library_dirs()[0]"
    pyarrow_LIBS_DIR
)
get_pyarrow_info(
    "pyarrow.cpp_build_info.so_version"
    pyarrow_SOVER
)

if (NOT pyarrow_VERSION OR NOT pyarrow_INCLUDE_DIR OR NOT pyarrow_LIBS_DIR OR NOT pyarrow_SOVER)
    set(pyarrow_FOUND NO)
    return()
endif ()

# TODO: check the version of the found pyarrow installation against the required versions.

set(pyarrow_FOUND YES)

if (NOT pyarrow_FIND_QUIETLY)
    message(STATUS "pyarrow version ${pyarrow_VERSION} (so version ${pyarrow_SOVER}) found")
    message(STATUS "pyarrow include directories: ${pyarrow_INCLUDE_DIR}")
    message(STATUS "pyarrow library directories: ${pyarrow_LIBS_DIR}")
endif ()

function (find_pyarrow_library name)
    cmake_parse_arguments(pyarrow_lib
        ""
        ""
        "NAMES;PATHS"
        ${ARGN}
    )

    find_library(${name} NO_DEFAULT_PATH REQUIRED
        NAMES ${pyarrow_lib_NAMES}
        PATHS ${pyarrow_lib_PATHS}
    )

    add_library(${name} SHARED IMPORTED)
    set_target_properties(${name} PROPERTIES
        IMPORTED_LOCATION ${${name}}
    )
    target_include_directories(${name} INTERFACE ${pyarrow_INCLUDE_DIR})

    if (NOT pyarrow_FIND_QUIETLY)
        message(STATUS "pyarrow library ${${name}} imported as \"${name}\"")
    endif ()
endfunction ()

find_pyarrow_library(arrow
    PATHS ${pyarrow_LIBS_DIR}
    NAMES
        libarrow.so
        libarrow.so.${pyarrow_SOVER}
)
find_pyarrow_library(arrow_python
    PATHS ${pyarrow_LIBS_DIR}
    NAMES
        libarrow_python.so
        libarrow_python.so.${pyarrow_SOVER}
)
find_pyarrow_library(parquet
    PATHS ${pyarrow_LIBS_DIR}
    NAMES
        libparquet.so
        libparquet.so.${pyarrow_SOVER}
)
