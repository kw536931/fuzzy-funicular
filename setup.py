"""
This script only contains complementary information to the pyproject.toml file. The common packaging
configurations are contained in that file.
"""

import os
from pathlib import Path
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name):
        super().__init__(name, sources=[])


class cmake_build_ext(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
        super().run()

    def build_cmake(self, ext):
        build_dir = Path(self.build_temp)
        build_dir.mkdir(parents=True, exist_ok=True)

        ext_path = Path(self.get_ext_fullpath(ext.name))
        cmake_args = [
            "-DBUILD_TESTING=OFF",
            "-DCMAKE_BUILD_TYPE=Release",
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + str(ext_path.parent.absolute()),
        ]

        # example of build args
        build_args = ["--", "-j4"]

        cwd = Path().absolute()
        try:
            os.chdir(str(build_dir))

            # CMake configure.
            self.spawn(["cmake", str(cwd)] + cmake_args)

            # CMake build.
            if not self.dry_run:
                self.spawn(["cmake", "--build", "."] + build_args)
        finally:
            os.chdir(str(cwd))


setup(
    ext_modules=[
        CMakeExtension("jsda.jsda_cpp"),
    ],
    cmdclass={
        "build_ext": cmake_build_ext,
    }
)
