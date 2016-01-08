from conans import ConanFile, CMake
from conans.tools import download, unzip


class Catch(ConanFile):
    name = "catch"
    version = "1.3.0"

    def source(self):
        zip_name = "catch.zip"
        download("https://github.com/philsquared/Catch/archive/v1.3.0.zip", zip_name)
        unzip(zip_name)

    def package(self):
        self.copy("*", dst="include", src="Catch-1.3.0/include")
