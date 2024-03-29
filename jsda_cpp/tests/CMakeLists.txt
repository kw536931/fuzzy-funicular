include(GoogleTest)

add_executable(jsda_tests
    # TODO: list your unit test source files here.
    VarianceAggregator.cpp
)
target_link_libraries(jsda_tests PRIVATE jsda_objects gmock_main)
set_target_properties(jsda_tests PROPERTIES
    CXX_STANDARD 20
)

gtest_discover_tests(jsda_tests)
