#pragma once

#include <filesystem>
#include <memory>

#include <arrow/table.h>

namespace jsda
{

class CsvLoader
{
public:
    explicit CsvLoader(std::filesystem::path path) noexcept;

    std::shared_ptr<arrow::Table> load() const;

private:
    std::filesystem::path path_;
};

} // namespace jsda
