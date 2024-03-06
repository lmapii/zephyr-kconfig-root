
# Locating `Kconfig` files

This is a repository demonstrating how to use or place `Kconfig` files. It uses freestanding applications - even though workspaces would definitely be the better solution. This becomes clear once looking at the final example when using Zephyr modules.

> **Note:** All examples specify the CMake variables in the `CMakeLists.txt` for demonstration purposes. As usual, the variables could also be set during build time.


## Replacing the application's Kconfig root directory

Demonstrated by [app_00_replace_root](./app_00_replace_root/CMakeLists.txt).

This example shows how to specify an alternative path for the `Kconfig` file that is otherwise automatically detected in the application's root directory using the CMake variable `KCONFIG_ROOT`. Instead of using its own `Kconfig` file, it uses the Kconfig file placed in [`kconfig-root`](./kconfig-root/Kconfig)

Notice that this is really only recommended as a lazy way to have the **very same** `Kconfig` file, e.g., for multiple samples. I'd not recommend this.


## Using `rsource` to source Kconfig files

Demonstrated by [app_01_rsource](./app_01_rsource/CMakeLists.txt).

Zephyr provides a [Kconfig extension `rsource`](https://docs.zephyrproject.org/latest/build/kconfig/extensions.html) which allows to source `Kconfig` files with relative paths.

In this approach, the application provides its own [`Kconfig`](./app_01_rsource/Kconfig) file in the application's root directory (automatically detected by Zephyr since we're not manipulating the `KCONFIG_ROOT` build variable). Within this `Kconfig` file it is possible to use `rsource` to source `Kconfig` files from different locations, e.g., the files in [`kconfig-rsource`](./kconfig-rsource/).

> **Note:** In contrast to [app_00_replace_root](./app_00_replace_root/CMakeLists.txt), the root `Kconfig` file **must** source `Kconfig.zephr`. Have a look at the detailed explanation in the [`Kconfig`](./app_01_rsource/Kconfig) file.


## Advanced: Using extra Zephyr modules

Demonstrated by [app_02_modules](./app_02_modules/CMakeLists.txt).

This is probably the cleanest but also the most advanced approach: Zephyr supports ["modules"](https://docs.zephyrproject.org/latest/develop/modules.html#module-integration-files-zephyr-module-yml), which are typically used to include external projects such as [Nanopb](https://github.com/nanopb/nanopb/blob/master/zephyr/module.yml).

In this approach we extend the build variable `EXTRA_ZEPHYR_MODULES` to point to a [dummy module](./extra-zephyr-modules/dummy/zephyr/module.yml), which also has its own [`Kconfig` file](./extra-zephyr-modules/dummy/Kconfig).

Please have a look at the documentation in the [application's `CMakeLists.txt`](./app_02_modules/CMakeLists.txt) and the [module's `module.yml` file](./extra-zephyr-modules/dummy/zephyr/module.yml).

> **Note:** This approach shines when switching to workspace applications, which is definitely the recommended way to work with Zephyr. Then it is no longer necessary to use `EXTRA_ZEPHYR_MODULES` since West will take care of all modules.
