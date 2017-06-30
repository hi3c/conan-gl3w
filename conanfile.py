from conans import ConanFile, CMake, tools
import os

SHA1="f1c961b4b35c86ca5fe7f6128442282ce32e431e"

class Gl3wConan(ConanFile):
    name = "gl3w"
    version = "git-f1c961b"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "CMakeLists.txt"

    def source(self):
        tools.download("https://github.com/skaslev/gl3w/archive/{}.zip".format(SHA1), "gl3w.zip")
        tools.unzip("gl3w.zip")
        os.remove("gl3w.zip")

    def build(self):
        cmake = CMake(self)
        os.mkdir("source_gen")
        self.run('cd source_gen && cmake ../gl3w-{} {}'.format(SHA1, cmake.command_line))
        self.run("cd source_gen && cmake --build . %s" % cmake.build_config)

        cmake.configure(defs={"GL3W_SRCDIR": os.path.join(self.conanfile_directory, "gl3w-" + SHA1)})
        cmake.build()


    def package(self):
        self.copy("*.h", dst="include", src="source_gen/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gl3w"]
        if self.settings.os == "Windows":
            self.cpp_info.libs.append("OpenGL32")
