# file_handler_py_package

A Python package for handling file operations and CSV processing.

## Description

This package provides convenient classes for reading, writing, and manipulating files, with specialized support for CSV operations. It includes `FileHandler` for general file operations and `CSVHandler` for CSV-specific functionality.

## Installation

You can install this package using pip:

```bash
# Install from local directory
pip install .

# Install in development/editable mode
pip install -e .
```

## Usage

After installation, you can import and use the package:

```python
from file_handler_py_package import FileHandler, CSVHandler

# Use FileHandler for general file operations
fh = FileHandler('myfile.txt')
content = fh.read()
fh.write('New content')
fh.append('Additional content')

# Use CSVHandler for CSV operations
csv_handler = CSVHandler('data.csv')
data = csv_handler.read_csv('data.csv')
csv_handler.write_csv(data)
```

## Package Structure

```text
file_handler_py_package/
├── file_handler_py_package/   # Package directory
│   ├── __init__.py            # Package initialization
│   ├── file_handler.py        # FileHandler class for general file operations
│   └── csv_handler.py         # CSVHandler class for CSV operations
├── pyproject.toml             # Modern Python project metadata (PEP 621)
├── setup.py                   # Setup script for backward compatibility
├── MANIFEST.in                # Specifies additional files to include
├── README.md                  # This file
├── LICENSE                    # License information
└── .gitignore                 # Git ignore rules
```

## Features

This package provides:

- **FileHandler**: A class for general file operations with methods for:
  - Reading files
  - Writing files
  - Appending to files
  - Checking file existence
  - Identifying file types by extension
  - Deleting files

- **CSVHandler**: A specialized class extending FileHandler with CSV-specific methods:
  - Reading CSV files into lists of dictionaries
  - Writing lists of dictionaries to CSV files
  - Support for custom delimiters
  - Configurable field names

- Modern `pyproject.toml` configuration (PEP 621)
- Backward-compatible `setup.py`
- Type hints for better IDE support
- Proper package structure
- Version information

## Requirements

- Python >= 3.7

## License

See LICENSE file for details.
