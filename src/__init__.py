"""Src package for the File Handler application."""
from src.data_manager.sub_menu import (display_file_handler_menu,
                                       display_database_handler_menu,
                                       display_settings_menu)
from src.data_manager.file_manager import FileManager
from src.data_manager.database_management_system import (
    DatabaseManagementSystem)
from src.utils import UserInterface, OpereatingSystem


__version__ = '1.0.0'
__author__ = 'Christian Schinkel'
__license__ = 'MIT License'
__all__ = ['FileManager',
           'DatabaseManagementSystem',
           'display_file_handler_menu',
           'display_database_handler_menu',
           'display_settings_menu',
           'UserInterface',
           'OpereatingSystem']
