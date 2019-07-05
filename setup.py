#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs

try:
    codecs.lookup("mbcs")
except LookupError:
    ascii = codecs.lookup("ascii")
    codecs.register(lambda name, enc=ascii: {True: enc}.get(name == "mbcs"))

VERSION = "0.1.0"
URL = "https://github.com/donbc/python-crowdwiz"

setup(
    name="crowdwiz",
    version=VERSION,
    description="Python library for crowdwiz",
    long_description=open("README.md").read(),
    download_url="{}/tarball/{}".format(URL, VERSION),
    author="Donbc Crowdwiz",
    author_email="donbc@protonmail.com",
    maintainer="Donbc Crowdwiz",
    maintainer_email="donbc@protonmail.com",
    url=URL,
    keywords=["crowdwiz", "library", "api", "rpc"],
    packages=["crowdwiz", "crowdwizapi", "crowdwizbase"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial",
    ],
    install_requires=open("requirements.txt").readlines(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
)
