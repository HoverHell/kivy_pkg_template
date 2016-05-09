#!/usr/bin/env python
# coding: utf8
"""
cx_Freeze-based packaging: setup file.

Currently, cx_Freeze does not go well with kivy. Apparently, some
Cython's hacks for circular imports (through pxd) didn't go well with
some cx_Freeze's hacks for importing. In kivy in particular,
kivy.properties (pxd) imports kivy._event for method signatures, and
kivy._event (pyx) import kivy.properties to use them all over the
place.
"""

import sys
from setuptools import setup as st_setup
from Cython.Build import cythonize
from cx_Freeze import setup as cx_setup
from cx_Freeze import Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
cx_build_options = dict(
    packages=[
        "kivy",
        "kivypkgtplapp",
    ],
    excludes=[],
    includes=[
    ],
    include_files=[
        "kivypkgtplapp/sampleapp.kv",
    ],
)

# base = 'Console'
base = 'Win32GUI' if sys.platform == 'win32' else None

ext_modules = cythonize([
    # "kivypkgtplapp/hello_cython.pyx",
    "kivypkgtplapp/*.pyx",
])

executables = [
    Executable(
        'kivypkgtplapp/main.py', base=base,
        targetName='example_app_kivypkgtpl'),
]

setup_kwargs = dict(
    name='template_kivy_packaging',
    version='1.0',
    description='',
    options=dict(build_exe=cx_build_options),
    ext_modules=ext_modules,
    executables=executables,
    packages=["kivypkgtplapp"],
)


def main():
    # To make sure cx_freeze finds the cython modules when doing
    # `build` (`build_exe`), have to build them and place them where
    # they can be imported - e.g. inplace.
    st_setup(
        name=setup_kwargs['name'],
        packages=setup_kwargs['packages'],
        ext_modules=ext_modules,
        options=dict(build_ext=dict(inplace=True)),
    )
    # cx_freeze actual
    cx_setup(**setup_kwargs)


if __name__ == '__main__':
    main()
