project(MyApp C CXX)
cmake_minimum_required(VERSION 3.3.2)

include(cmake/App.cmake)
include(cmake/FMT.cmake)

set(SOURCES "src/IOUtility.h"
            "src/IOUtility.cpp"
            "src/MyApp.h"
            "src/MyApp.cpp"
            "src/Student.h"
            "src/Student.cpp"
            "src/main.cpp")

add_app("${SOURCES}")
