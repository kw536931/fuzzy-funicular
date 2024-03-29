#include <cstddef>
#include <filesystem>
#include <memory>
#include <span>
#include <utility>

#include <arrow/table.h>
#include <arrow/python/pyarrow.h>
#include <arrow/python/pyarrow_api.h>
#include <pybind11/cast.h>
#include <pybind11/detail/common.h>
#include <pybind11/pybind11.h>
#include <pybind11/pytypes.h>
#include <pybind11/numpy.h>

#include "jsda/Aggregators.hpp"
#include "jsda/Loaders.hpp"

namespace pybind11::detail
{

template <>
struct type_caster<std::shared_ptr<arrow::Table>>
{
    PYBIND11_TYPE_CASTER(std::shared_ptr<arrow::Table>, const_name("pyarrow::Table")); // NOLINT

    bool load(handle src, bool allowImplicitConversions)
    {
        auto *source = src.ptr();
        if (!arrow::py::is_table(source))
        {
            return false;
        }

        auto unwrapResult = arrow::py::unwrap_table(source);
        if (!unwrapResult.ok())
        {
            return false;
        }

        value = std::move(*unwrapResult);
        return true;
    }

    // NOLINTNEXTLINE(performance-unnecessary-value-param)
    static handle cast(std::shared_ptr<arrow::Table> table, return_value_policy policy, handle parent)
    {
        return arrow::py::wrap_table(table);
    }
};

} // namespace pybind11::detail

namespace
{

template <typename Aggregator>
class AggregatorAdaptor
{
public:
    template <typename... Args>
    explicit AggregatorAdaptor(Args &&...args) noexcept
        : aggregator_(std::forward<Args>(args)...)
    {
    }

    AggregatorAdaptor(const AggregatorAdaptor &) noexcept = default;
    AggregatorAdaptor(AggregatorAdaptor &&) noexcept = default;

    ~AggregatorAdaptor() noexcept = default;

    AggregatorAdaptor &operator=(const AggregatorAdaptor &) &noexcept = default;
    AggregatorAdaptor &operator=(AggregatorAdaptor &&) &noexcept = default;

    float aggregate(pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast> array)
    {
        std::span<const float> arraySpan{array.mutable_data(), static_cast<std::size_t>(array.size())};
        return aggregator_.aggregate(arraySpan);
    }

private:
    Aggregator aggregator_;
};

} // namespace

PYBIND11_MODULE(jsda_cpp, m) // NOLINT
{
    m.doc() = "Jiaqi Simple Data Aggregator";

    using CppVarianceAggregator = AggregatorAdaptor<jsda::VarianceAggregator>;
    pybind11::class_<CppVarianceAggregator>(m, "CppVarianceAggregator")
        .def(pybind11::init())
        .def("aggregate", &CppVarianceAggregator::aggregate);

    pybind11::class_<jsda::CsvLoader>(m, "CppCsvLoader")
        .def(pybind11::init<const std::filesystem::path &>())
        .def("load", &jsda::CsvLoader::load);
}
