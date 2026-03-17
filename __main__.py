"""The main entry point for the application."""
from src.data_manager.sub_menu import (display_file_handler_menu,
                                       display_database_handler_menu,
                                       display_settings_menu)
from src.data_manager.file_manager import FileManager
from src.data_manager.database_management_system import (
    DatabaseManagementSystem)
from src.utils import UserInterface

__version__ = "1.0.0"
__author__ = "Christian Schinkel"
__license__ = "MIT License"


def main() -> None:
    """The main function."""
    # Create an instance of the UserInterface class
    ui = UserInterface()
    # Display application information
    ui.show_app_info(version=__version__, author=__author__, lic=__license__)
    # Wait for a moment before clearing the console
    ui.wait_and_clear_console(seconds=2)
    # Show Main Menu
    display_main_menu(ui)


def display_main_menu(ui):
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
            display_file_handler_menu(ui, fm)
        elif choice == "2":
            # Import the database handler menu and call it
            display_database_handler_menu(ui, dbms)
        elif choice == "3":
            # Import the settings menu and call it
            display_settings_menu(ui, fm)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            is_running = False
            ui.wait_and_clear_console(seconds=2)
            ui.clear_console()
        else:
            print("Invalid choice. Please try again.")
            ui.wait_and_clear_console(seconds=2)


if __name__ == "__main__":
    main()
