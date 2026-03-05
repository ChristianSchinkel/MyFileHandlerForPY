"""
Setup script for file_handler_py_package.

This file provides backward compatibility for older pip versions.
For modern installations, pyproject.toml is preferred.
"""

from pathlib import Path
import setuptools

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="file_handler_py_package",
    version="0.1.0",
    author="Christian Schinkel",
    author_email="christian.schinkel@me.com",
    description="A Python package for handling files and CSV operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChristianSchinkel/MyFileHandlerForPY",
    packages=setuptools.find_packages(),
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
    keywords="file handler csv file-operations",
)
