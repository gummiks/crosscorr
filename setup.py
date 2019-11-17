#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:13:04 2019

@author: rterrien
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccf", # Replace with your own username
    version="0.0.1",
    author="Ryan Terrien",
    author_email="rterrien@carleton.edu",
    description="CCF Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
#    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
#        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)