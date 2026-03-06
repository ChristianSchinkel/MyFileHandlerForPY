"""
file_handler_py_package: A basic Python package template.

This package provides a simple example of a Python package structure
that can be installed via pip install.
"""

from .file_manager import FileManager
from .csv_manager import CSVManager

__version__ = "0.1.0"
__author__ = "Christian Schinkel"
__all__ = ["FileManager", "CSVManager"]


def main():
    """A simple main function to demonstrate the package."""
    print("Welcome to the file_handler_py_package!")


if __name__ == "__main__":
    main()
