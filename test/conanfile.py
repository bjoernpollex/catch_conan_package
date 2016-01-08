from os.path import join
from conans import ConanFile, CMake


class CatchPackageTest(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "catch/1.3.0@bjoern/testing"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake . %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.run(join(".", "bin", "test"))
