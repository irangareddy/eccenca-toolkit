#!/usr/bin/env python
"""setup.py for cmemc."""

from setuptools import setup, find_packages

setup(
    name="eccenca-toolkit",
    version="0.1",
    author="Ranga Reddy Nukala",
    author_email="sairangareddy22@gmail.com",
    url="https://eccenca.com/",
    description="Command line client for eccenca Developers",
    # long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="Apache 2.0",
    entry_points={
        "console_scripts": [
            "eckit = toolkit:cli",
        ],
    },
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Testing",
        "Topic :: Database",
        "Topic :: Utilities",
    ],
)
