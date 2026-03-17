# MyFileHandlerForPY

A Python CLI application for file and SQLite database management.

## Description

This project provides a menu-driven console app to manage files, basic
database table creation, and app-related data under `app_data/`.

Core modules:

- `FileManager` in `src/data_manager/file_manager.py`
- `DatabaseManagementSystem` in `src/data_manager/database_management_system.py`
- `UserInterface` in `src/utils/user_interface.py`

## Installation

Install from the project root:

```bash
pip install .
```

For editable development:

```bash
pip install -e .
```

## Run The Application

Start the CLI app:

```bash
python __main__.py
```

## Usage (Imports)

Example imports based on the current source tree:

```python
from src.data_manager.file_manager import FileManager
from src.data_manager.database_management_system import DatabaseManagementSystem
from src.utils.user_interface import UserInterface
```

## Project Structure

```text
MyFileHandlerForPY/
├── __main__.py
├── app_data/
│   ├── persistence/
│   ├── resources/
│   └── user_defaults/
├── src/
│   ├── __init__.py
│   ├── data_manager/
│   │   ├── __init__.py
│   │   ├── database_management_system.py
│   │   ├── file_manager.py
│   │   └── sub_menu.py
│   └── utils/
│       ├── __init__.py
│       ├── os_check.py
│       └── user_interface.py
├── tests/
├── pyproject.toml
├── setup.py
└── README.md
```

## Features

- File operations:
  - Create file
  - Read file
  - Update file
  - Delete file
  - Import one or many files from another directory
- Database operations:
  - SQLite connection and table creation via schema input
  - Data insertion helpers
- Settings operations:
  - Import user defaults file
  - Remove user defaults, resource files, and persistence files
- Console helpers:
  - Welcome banner and app metadata display
  - Wait/clear console utilities

## Requirements

- Python >= 3.7
- `InputController>=0.2`

## License

MIT License. See `LICENSE` for details.
