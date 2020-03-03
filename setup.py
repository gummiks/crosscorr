#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:13:04 2019

@author: rterrien
"""

import setuptools
from numpy.distutils.core import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

lib1 = Extension(name='ccf.CCF_1d',sources=['src/CCF_1d.f'])
lib2 = Extension(name='ccf.CCF_3d',sources=['src/CCF_3d.f'])
lib3 = Extension(name='ccf.CCF_pix',sources=['src/CCF_pix.f'])


setup(
    name="ccf", # Replace with your own username
    version="0.0.1",
    author="Ryan Terrien",
    author_email="rterrien@carleton.edu",
    description="CCF Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
#    url="https://github.com/pypa/sampleproject",
    #packages=setuptools.find_packages(where='./src'),
    package_dir={"ccf":"src"},
    packages=setuptools.find_packages(),#[''],#setuptools.find_packages(),
    py_modules=['ccf.mask','ccf.utils','ccf.airtovac'],
    #py_modules=['ccf.mask'],
    #packages=['mask'],
    ext_modules = [lib1,lib2,lib3],
    classifiers=[
        "Programming Language :: Python :: 2",
#        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
