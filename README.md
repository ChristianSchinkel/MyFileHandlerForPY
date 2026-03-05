# basic_py_package

Basic Python Package with information and all needed files to install it via "pip install".

## Description

This is a template/example of a basic Python package that demonstrates the minimal structure needed to create a package that can be installed using pip.

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
import basic_py_package

# Use the provided functions
print(basic_py_package.greet("World"))  # Output: Hello, World!
print(basic_py_package.add(2, 3))       # Output: 5
print(basic_py_package.multiply(4, 5))  # Output: 20
```

## Package Structure

```
basic_py_package/
├── basic_py_package/      # Package directory
│   └── __init__.py        # Package initialization with example functions
├── pyproject.toml         # Modern Python project metadata (PEP 621)
├── setup.py               # Setup script for backward compatibility
├── MANIFEST.in            # Specifies additional files to include
├── README.md              # This file
├── LICENSE                # License information
└── .gitignore             # Git ignore rules
```

## Features

This package includes:
- Modern `pyproject.toml` configuration (PEP 621)
- Backward-compatible `setup.py`
- Example functions with docstrings
- Proper package structure
- Version information

## Requirements

- Python >= 3.7

## License

See LICENSE file for details.
