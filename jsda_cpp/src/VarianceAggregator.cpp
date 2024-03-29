#include "jsda/Aggregators.hpp"

#include <functional>
#include <limits>
#include <numeric>

namespace jsda
{

// NOLINTNEXTLINE(readability-convert-member-functions-to-static)
float VarianceAggregator::aggregate(std::span<const float> data) const noexcept
{
    if (data.empty())
    {
        return std::numeric_limits<float>::quiet_NaN();
    }

    auto n = data.size();
    auto u = std::reduce(data.begin(), data.end(), 0.0) / static_cast<double>(n);
    auto u2 =
        std::transform_reduce(data.begin(), data.end(), 0.0, std::plus<double>{}, [](double x) { return x * x; }) /
        static_cast<double>(n);
    return static_cast<float>(u2 - u * u);
}

} // namespace jsda
