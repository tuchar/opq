cmake_minimum_required(VERSION 3.0)
project(Triggering)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -DBOOST_LOG_DYN_LINK")
set(LIBS "${CMAKE_CXX_FLAGS} ")

include_directories(${CMAKE_SOURCE_DIR}/lib)
include_directories(${CMAKE_SOURCE_DIR}/filters)
include_directories(${CMAKE_SOURCE_DIR}/proto)

FILE(GLOB sources ${CMAKE_SOURCE_DIR}/src/*.cpp)
FILE(GLOB headers ${CMAKE_SOURCE_DIR}/lib/*.hpp)

FILE(GLOB filter_src ${CMAKE_SOURCE_DIR}/filters/*.cpp)
FILE(GLOB filter_inc ${CMAKE_SOURCE_DIR}/filters/*.hpp)

FILE(GLOB proto_src ${CMAKE_SOURCE_DIR}/proto/*.cc)
FILE(GLOB proto_inc ${CMAKE_SOURCE_DIR}/proto/*.h)

FILE(GLOB mongoose_src ${CMAKE_SOURCE_DIR}/mongoose/*.c)
FILE(GLOB mongoose_inc ${CMAKE_SOURCE_DIR}/mongoose/*.h)


add_executable(Triggering ${sources} ${headers} ${filter_src} ${filter_inc} ${proto_src} ${proto_inc} ${mongoose_src} ${mongoose_inc})
target_link_libraries (Triggering pthread)
target_link_libraries (Triggering protobuf)
target_link_libraries (Triggering zmqpp)
target_link_libraries (Triggering zmq)
target_link_libraries (Triggering boost_log_setup)
target_link_libraries (Triggering boost_log)
target_link_libraries (Triggering boost_system)
target_link_libraries (Triggering boost_thread)

add_executable(Triggering-sim ${sources} ${headers} ${filter_src} ${filter_inc} ${proto_src} ${proto_inc} ${mongoose_src} ${mongoose_inc})
target_link_libraries (Triggering-sim pthread)
target_link_libraries (Triggering-sim protobuf)
target_link_libraries (Triggering-sim zmqpp)
target_link_libraries (Triggering-sim zmq)
target_link_libraries (Triggering-sim boost_log_setup)
target_link_libraries (Triggering-sim boost_log)
target_link_libraries (Triggering-sim boost_system)
target_link_libraries (Triggering-sim boost_thread)
set_target_properties(Triggering-sim PROPERTIES COMPILE_FLAGS "-DOPQ_DEBUG")
