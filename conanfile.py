from contextlib import closing
from tarfile import open as taropen
from urllib2 import urlopen

from conans import ConanFile


class Catch(ConanFile):
    name = "catch"
    version = "1.3.0"

    def source(self):
        release_url = "https://github.com/philsquared/Catch/archive/v{0}.tar.gz".format(self.version)
        with closing(urlopen(release_url)) as dl:
            with taropen(mode='r|gz', fileobj=dl) as archive:
                archive.extractall()

    def package(self):
        self.copy("*", dst="include", src="Catch-{0}/include".format(self.version))
