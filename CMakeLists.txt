project(gl3w)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(gl3w STATIC source_gen/src/gl3w.c)

target_include_directories(gl3w PRIVATE source_gen/include)