# file_manager_py_package

A Python package for handling file operations and CSV processing.

## Description

This package provides convenient classes for reading, writing, and manipulating files, with specialized support for CSV operations. It includes `FileManager` for general file operations and `CSVManager` for CSV-specific functionality.

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
from file_manager_py_package import FileManager, CSVManager

# Use FileManager for general file operations
fm = FileManager('myfile.txt')
content = fm.read()
fm.write('New content')
fm.append('Additional content')

# Use CSVManager for CSV operations
csv_manager = CSVManager('data.csv')
data = csv_manager.read_csv('data.csv')
csv_manager.write_csv(data)
```

## Package Structure

```text
file_manager_py_package/
├── file_manager_py_package/   # Package directory
│   ├── __init__.py            # Package initialization
│   ├── file_manager.py        # FileManager class for general file operations
│   ├── csv_manager.py         # CSVManager class for CSV operations
│   ├── directory_manager.py   # DirectoryManager class for directory operations
│   └── memory_manager.py      # MemoryManager class for storage management
├── utils/                     # Utility modules
│   └── start_end.py           # Application startup and cleanup functions
├── pyproject.toml             # Modern Python project metadata (PEP 621)
├── setup.py                   # Setup script for backward compatibility
├── MANIFEST.in                # Specifies additional files to include
├── README.md                  # This file
├── LICENSE                    # License information
└── __main__.py                # Application entry point
```

## Features

This package provides:

- **FileManager**: A class for general file operations with methods for:
  - Reading files
  - Writing files
  - Appending to files
  - Checking file existence
  - Identifying file types by extension
  - Deleting files

- **CSVManager**: A specialized class extending FileManager with CSV-specific methods:
  - Reading CSV files into lists of dictionaries
  - Writing lists of dictionaries to CSV files
  - Support for custom delimiters
  - Configurable field names

- **DirectoryManager**: A class for directory operations with methods for:
  - Checking directory existence
  - Getting directory contents
  - Setting directory paths

- **MemoryManager**: A class for application data storage with methods for:
  - Reading and writing storage files
  - Copying files from source directories
  - Clearing application data

- Modern `pyproject.toml` configuration (PEP 621)
- Backward-compatible `setup.py`
- Type hints for better IDE support
- Proper package structure
- Version information

## Requirements

- Python >= 3.7

## License

See LICENSE file for details.
