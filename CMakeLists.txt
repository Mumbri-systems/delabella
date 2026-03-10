cmake_minimum_required(VERSION 2.6)
cmake_policy(SET CMP0048 "NEW")

project(delabella LANGUAGES CXX VERSION 1.0)

include(GNUInstallDirs)

add_library(${PROJECT_NAME} ${PROJECT_SOURCE_DIR}/delabella.cpp)

target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_SOURCE_DIR})

add_library(delabella::delabella ALIAS delabella)

install(FILES ${PROJECT_SOURCE_DIR}/delabella.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(TARGETS ${PROJECT_NAME}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR})
