#include "jsda/Aggregators.hpp"

#include <cmath>
#include <vector>

#include <gtest/gtest.h>

TEST(VarianceAggregatorTests, aggregate) // NOLINT
{
    jsda::VarianceAggregator aggregator;
    std::vector<float> data{1, 2, 3, 4, 5}; // NOLINT(*-magic-numbers)

    auto result = aggregator.aggregate(data);
    ASSERT_FLOAT_EQ(result, 2.0);
}

TEST(VarianceAggregatorTests, aggregateEmptyInput) // NOLINT
{
    jsda::VarianceAggregator aggregator;
    std::vector<float> data;

    auto result = aggregator.aggregate(data);
    ASSERT_TRUE(std::isnan(result));
}
