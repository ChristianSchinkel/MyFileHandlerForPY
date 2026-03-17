"""The main entry point for the application."""
from src.data_manager.sub_menu import (display_file_handler_menu,
                                       display_database_handler_menu,
                                       display_settings_menu)
from src.data_manager.file_manager import FileManager
from src.data_manager.database_management_system import (
    DatabaseManagementSystem)


def main() -> None:
    """The main function."""
    show_app_info()
    # Show Main Menu
    display_main_menu()


def display_main_menu():
    """Displays the main menu and handles user input."""
    fm = FileManager()
    dbms = DatabaseManagementSystem()

    is_running = True
    while is_running:
        print("""Main Menu:\n
1. File Handler\n
2. Database Handler\n
3. Settings\n
4. Exit
          """)
        choice = input("Please select an option: ")
        if choice == "1":
            # Import the file handler menu and call it
            display_file_handler_menu(fm)
        elif choice == "2":
            # Import the database handler menu and call it
            display_database_handler_menu(dbms)
        elif choice == "3":
            # Import the settings menu and call it
            display_settings_menu(fm)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            is_running = False
        else:
            print("Invalid choice. Please try again.")


def show_app_info():
    """Displays information about the application."""
    print("""
+----------------------------------------------------------+
|Welcome to the File Handler for Python!                   |
+----------------------------------------------------------+
|This application allows you to manage files and databases.|
|Version: 1.0.0                                            |
|Author: Christian Schinkel                                |
|License: MIT License                                      |
+==========================================================+
          """)


if __name__ == "__main__":
    main()
