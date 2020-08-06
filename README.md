# Sphinx Domain for Modern CMake

This is taken directly from the Kitware git repository's Utilities directory.
The original [sphinxcontrib-cmakedomain] has not been touched in quite some and
as a result it wildly out of date. Documenting CMake domain entities in
projects is painful otherwise. This works *exactly* in the same way as Kitware,
so some time might be needed to study their approach to these problems.

This repository is under the same License as all of CMake, which is the
BSD-3-Clause license.

I will do my best to keep this module in sync with the one that Kitware uses
themselves.

🚨🚨🚨
Any issues you run into with this plugin must be reported to [Kitware]
🚨🚨🚨

*I will* ⛔**not**⛔ _make any effort to modify the module, **only**_
📦*packaging*📦 *improvements.*

# Installation

## PyPI

This domain is available via PyPI. Install it directly via `pip`:

```
$ pip install sphinxcontrib-moderncmakedomain
```

Alternatively, place it inside of your `setup.py`, `pyproject.toml`,
`requirements.txt` or whatever system it is that you use to declare and manage
your dependencies. The version available will be in the same *major* version as
the latest CMake release.

## Git

This module is installable via `pip` and GitHub directly as well

```
$ pip install git+https://github.com/slurps-mad-rips/moderncmakedomain.git
```

# Usage

To enable the use of the `moderncmakedomain`, add
`sphinxcontrib.moderncmakedomain` to the `extensions` variable of your
`conf.py` file:

```python
extensions = [..., 'sphinxcontrib.moderncmakedomain', ...]
```

The plugin currently provides several directives and refrences. These are
documented below.

## Directives

|     directive      |                      description                    |
|:------------------:|:----------------------------------------------------|
| `cmake:variable::` | For a basic variable                                |
| `cmake:command::`  | For a function                                      |
| `cmake-module::`   | Autodoc style extractor (takes a relative filepath) |
| `cmake:envvar::`   | For environment variables                           |

To declare any of the references found below, they must be placed into a
directory with the same name under the sphinx SOURCEDIR/master doc. Thus,
`prop_tgt/MY_PERSONAL_PROPERTY.rst` can be referred to with
``:prop_tgt:`MY_PERSONAL_PROPERTY` ``. This is currently the *only* way CMake
permits declaring new properties.

## References

Each reference below can be placed into a directory with the same name to
document custom extensions provided by your CMake libraries.

|      ref       |                   description                      |
|:--------------:|:---------------------------------------------------|
| `:variable:`   | Refer to a CMake variable                          |
| `:command:`    | Refer to a CMake command                           |
| `:envvar:`     | Refers to an environment variable                  |
| `:cpack_gen:`  | Refers to CPack generators                         |
| `:generator:`  | Refers to a build file generator                   |
| `:guide:`      | Used to refer to a "guide" page                    |
| `:manual:`     | Used to refer to a "manual" page (like `cmake(1)`) |
| `:policy:`     | Refers to CMake Policies                           |
| `:module:`     | Refers to CMake Modules                            |
| `:prop_tgt:`   | For target properties                              |
| `:prop_test:`  | For test properties                                |
| `:prop_sf:`    | For source file properties                         |
| `:prop_gbl:`   | For global properties                              |
| `:prop_dir:`   | For directory properties                           |
| `:prop_inst:`  | For installed file properties                      |
| `:prop_cache:` | For cache properties                               |

[sphinxcontrib-cmakedomain]: https://github.com/sphinx-contrib/cmakedomain
[Kitware]: https://gitlab.kitware.com/
