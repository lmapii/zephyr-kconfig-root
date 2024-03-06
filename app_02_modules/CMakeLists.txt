cmake_minimum_required(VERSION 3.20.0)

# The best way to include multiple Kconfig file is to use Zephyr extra modules. The
# EXTRA_ZEPHYR_MODULES build time variable allows to define a list of extra modules, which can
# include plain Kconfig files but also sources (and their own CMakeLists.txt)
# https://docs.zephyrproject.org/latest/develop/modules.html#module-integration-files-zephyr-module-yml
#
# A good reference is the integrations of "Nanopb" in Zephyr, though that also makes use of the
# "MODULE_EXT_ROOT": Only the 'module.yaml' is part of Nanopb's repository:
# https://github.com/nanopb/nanopb/blob/master/zephyr/module.yml
# The Kconfig and CMakeLists.txt are part of the Zephyr repository:
# https://github.com/zephyrproject-rtos/zephyr/tree/main/modules/nanopb
#
# In this example, the module.yml is part of the extra Zephyr module and thus placed in the
# same location as the module itself.

list(
    APPEND
    EXTRA_ZEPHYR_MODULES
    "${CMAKE_CURRENT_SOURCE_DIR}/../extra-zephyr-modules/dummy"
)
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
