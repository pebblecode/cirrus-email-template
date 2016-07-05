# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements
import pip.download
import os
import glob

try:
    long_description = open("README.asciidoc").read()
except IOError:
    long_description = ""

install_requires = []

setup(
    name="inoket-email-templates",
    version="1.0.0",
    description="Email Templates for Inoket",
    license="MIT",
    author="pebble {code}",
    packages=['inoket-email-templates'],
    install_requires=install_requires,
    long_description=long_description,
    package_data={
        'inoket-email-templates': ['assets/*.html']},
    classifiers=[
        "Programming Language :: HTML",
    ]
)
