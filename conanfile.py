from conans import ConanFile
from conans.tools import download, unzip


class Catch(ConanFile):
    name = "catch"
    version = "1.3.0"

    def source(self):
        zip_name = "catch.zip"
        download("https://github.com/philsquared/Catch/archive/v{0}.zip".format(self.version),
                 zip_name)
        unzip(zip_name)

    def package(self):
        self.copy("*", dst="include", src="Catch-{0}/include".format(self.version))
