cmake_minimum_required(VERSION 3.20)

project(Transversal)

set(CMAKE_FIND_LIBRARY_SUFFIXES ".a")

# Boinc
find_path(BOINC_INCLUDE_DIR NAMES boinc_api.h PATHS /usr/include/boinc)
if (NOT BOINC_INCLUDE_DIR)
    message(FATAL_ERROR "BOINC API not found. Set up boinc-client-dev or set up BOINC_INCLUDE_DIR")
else()
	message(STATUS "BOINC API found: ${BOINC_INCLUDE_DIR}")
endif()

find_library(BOINC_LIBRARY_API NAMES boinc_api)
find_library(BOINC_LIBRARY NAMES boinc)
if (NOT BOINC_LIBRARY OR NOT BOINC_LIBRARY_API)
    message(FATAL_ERROR "BOINC API or BOINC not found. Set up boinc-client-dev or set up BOINC_LIBRARY (${BOINC_LIBRARY} or BOINC_LIBRARY_API (${BOINC_LIBRARY_API}")
else()
	message(STATUS "BOINC_LIBRARY found: ${BOINC_LIBRARY}\n BOINC_LIBRARY_API found: ${BOINC_LIBRARY_API}")
endif()

include_directories(${BOINC_INCLUDE_DIR})

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set_property(GLOBAL PROPERTY PREDEFINED_TARGETS_FOLDER "cmake")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_CURRENT_SOURCE_DIR}/bin.dbg)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/bin.rel)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELWITHDEBINFO ${CMAKE_CURRENT_SOURCE_DIR}/bin.relwithdbg)

SET(DIR_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src")
SET(DIR_HEADERS "${CMAKE_CURRENT_SOURCE_DIR}/include")

file(GLOB_RECURSE HEADERS CONFIGURE_DEPENDS "${DIR_HEADERS}/*.hpp")
file(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS "${DIR_SOURCES}/*.cpp")

# SET(DIR_CXXOPTS_HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/../../thirdparty/cxxopts/include)
# file(GLOB_RECURSE CXXOPTS_HEADERS CONFIGURE_DEPENDS "${DIR_CXXOPTS_HEADERS}/*.hpp")

add_executable(Transversal main.cpp ${SOURCES})
target_link_libraries(Transversal PRIVATE ${BOINC_LIBRARY_API})
target_link_libraries(Transversal PRIVATE ${BOINC_LIBRARY})
target_include_directories(Transversal PUBLIC ${DIR_HEADERS})
# target_include_directories(Transversal PUBLIC ${DIR_CXXOPTS_HEADERS})
