project(MyApp C CXX)
cmake_minimum_required(VERSION 3.3.2)

include(cmake/App.cmake)

set(SOURCES "src/MyApp.h"
            "src/IOUtility.h"
            "src/IOUtility.cpp"
            "src/MyApp.cpp"
            "src/main.cpp")

add_app("${SOURCES}")