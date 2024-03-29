#pragma once

#include <span>

namespace jsda
{

class VarianceAggregator
{
public:
    float aggregate(std::span<const float> data) const noexcept;
};

} // namespace jsda
