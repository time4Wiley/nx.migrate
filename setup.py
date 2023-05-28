#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Wei Sun"
__copyright__ = "Copyright (C) 2019 GFLoan Co. LTD"
__license__ = "Private"
__version__ = "1.0"

import setuptools

long_description = ""

setuptools.setup(
    name="nx_migrate".replace("_", "."),
    version="1.0.0",
    author="Sun Wei",
    author_email="sunwei415@126.com",
    description="nx_migrate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "argparse",
    ],
    entry_points={"console_scripts": ["nx_migrate=nx_migrate.nx_migrate:main"]},
)
pass
