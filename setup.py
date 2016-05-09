#!/usr/bin/env python
# coding: utf8

from setuptools import setup
from setuptools import find_packages
from Cython.Build import cythonize


setup_kwargs = dict(
    name="template_kivy_packaging",
    version="1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'example_app_kivypkgtpl = kivypkgtplapp.main:main',
        ],
    },
    install_requires=['six', 'Kivy', 'Cython'],
    dependency_links=[
        # # Example:
        # 'https://github.com/sashka/atomicfile/tarball/master#egg=atomicfile',
    ],
    ext_modules=cythonize([
        # "kivypkgtplapp/hello_cython.pyx",
        "kivypkgtplapp/*.pyx",
    ]),
)


if __name__ == '__main__':
    setup(**setup_kwargs)
