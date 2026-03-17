"""
Setup script for MyFileHandlerForPY.

This file provides backward compatibility for older pip versions.
For modern installations, pyproject.toml is preferred.
"""

from pathlib import Path
import setuptools

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="myfilehandlerforpy",
    version="1.0.0",
    author="Christian Schinkel",
    author_email="christian.schinkel@me.com",
    description="A Python application for file and database management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChristianSchinkel/MyFileHandlerForPY",
    packages=["src", "src.data_manager", "src.utils"],
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
    install_requires=[
        "InputController>=0.2",
    ],
    keywords="file handler csv file-operations",
)
