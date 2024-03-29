add_library(jsda_objects OBJECT)
target_sources(jsda_objects
    PUBLIC
        # TODO: list your header files here.
        include/jsda/Aggregators.hpp
        include/jsda/Loaders.hpp
    PRIVATE
        # TODO: list your source code files here.
        src/CsvLoader.cpp
        src/VarianceAggregator.cpp
)
target_include_directories(jsda_objects PUBLIC include)
target_link_libraries(jsda_objects PUBLIC arrow)
set_target_properties(jsda_objects PROPERTIES
    CXX_STANDARD 20
    POSITION_INDEPENDENT_CODE ON
)

add_library(jsda MODULE src/bindings/Module.cpp)
target_link_libraries(jsda PRIVATE
    arrow_python
    jsda_objects
    Python3::Module
    pybind11::headers
)
set_target_properties(jsda PROPERTIES
    CXX_STANDARD 20
    LIBRARY_OUTPUT_NAME jsda_cpp
    PREFIX ""
    SUFFIX ".cpython-310-x86_64-linux-gnu.so"
)

if (BUILD_TESTING)
    add_subdirectory(tests)
endif ()
