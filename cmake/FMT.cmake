set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON) 
add_subdirectory(${CMAKE_SOURCE_DIR}/src/plugins/fmt/)
include_directories("${CMAKE_SOURCE_DIR}/src/plugins/fmt/include/")
# include(${CMAKE_ROOT}/Modules/ExternalProject.cmake)

# # fmt
# set(FMT_ROOT "${CMAKE_BINARY_DIR}/fmt/")
# set(FMT_INCLUDE_DIR "${FMT_ROOT}/include")

# ExternalProject_Add(fmt
#   PREFIX ${FMT_ROOT}/prefix
#   GIT_REPOSITORY https://github.com/fmtlib/fmt.git
#   CONFIGURE_COMMAND ""
#   BUILD_COMMAND ""
#   INSTALL_COMMAND ""
#   LOG_DOWNLOAD ON
# )