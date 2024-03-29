#include "jsda/Loaders.hpp"

#include <filesystem>
#include <utility>

#include <arrow/io/api.h>
#include <arrow/csv/api.h>

namespace jsda
{

CsvLoader::CsvLoader(std::filesystem::path path) noexcept
    : path_(std::move(path))
{
}

std::shared_ptr<arrow::Table> CsvLoader::load() const
{
    const auto &ioCtx = arrow::io::default_io_context();
    auto input = arrow::io::ReadableFile::Open(path_).ValueOrDie();

    auto reader =
        arrow::csv::TableReader::Make(ioCtx, input, arrow::csv::ReadOptions::Defaults(),
                                      arrow::csv::ParseOptions::Defaults(), arrow::csv::ConvertOptions::Defaults())
            .ValueOrDie();
    return reader->Read().ValueOrDie();
}

} // namespace jsda
