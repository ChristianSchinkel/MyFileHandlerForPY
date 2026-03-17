"""Data Manager for handling file and database operations."""
from .file_manager import FileManager
from .database_management_system import DatabaseManagementSystem
from .sub_menu import (display_file_handler_menu,
                       display_database_handler_menu,
                       display_settings_menu)


__version__ = '1.0.0'
__author__ = 'Christian Schinkel'
__license__ = 'MIT License'
__all__ = ['FileManager',
           'DatabaseManagementSystem',
           'display_file_handler_menu',
           'display_database_handler_menu',
           'display_settings_menu']
