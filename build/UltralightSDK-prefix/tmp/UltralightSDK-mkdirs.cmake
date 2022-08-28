# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "D:/coding/c++/year2/PBL02/build/SDK"
  "D:/coding/c++/year2/PBL02/build/UltralightSDK-prefix/src/UltralightSDK-build"
  "D:/coding/c++/year2/PBL02/build/UltralightSDK-prefix"
  "D:/coding/c++/year2/PBL02/build/UltralightSDK-prefix/tmp"
  "D:/coding/c++/year2/PBL02/build/UltralightSDK-prefix/src/UltralightSDK-stamp"
  "D:/coding/c++/year2/PBL02/build/UltralightSDK-prefix/src"
  "D:/coding/c++/year2/PBL02/build/UltralightSDK-prefix/src/UltralightSDK-stamp"
)

set(configSubDirs Debug;Release;MinSizeRel;RelWithDebInfo)
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "D:/coding/c++/year2/PBL02/build/UltralightSDK-prefix/src/UltralightSDK-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "D:/coding/c++/year2/PBL02/build/UltralightSDK-prefix/src/UltralightSDK-stamp${cfgdir}") # cfgdir has leading slash
endif()
