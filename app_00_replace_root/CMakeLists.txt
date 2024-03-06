cmake_minimum_required(VERSION 3.20.0)

# It is possible to _entirely_ change the KCONFIG_ROOT. Do this only if you really want to
# have the very same Kconfig for projects, but not if you want to extend it with possible features.
# https://docs.zephyrproject.org/latest/develop/modules.html
set(KCONFIG_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/../kconfig-root/Kconfig)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(
    EmptyApp
    VERSION 0.1
    DESCRIPTION "Dummy Kconfig Zephyr application."
    LANGUAGES C
)

target_sources(
    app
    PRIVATE
    src/main.c
)
