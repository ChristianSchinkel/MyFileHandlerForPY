"""
Setup script for basic_py_package.

This file provides backward compatibility for older pip versions.
For modern installations, pyproject.toml is preferred.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="basic_py_package",
    version="0.1.0",
    author="Christian Schinkel",
    author_email="christian@example.com",
    description="A basic Python package template that can be installed via pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChristianSchinkel/basic_py_package",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    keywords="example package template basic",
)
