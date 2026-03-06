"""Start and end functions for the application."""
from InputController.inputController import InputController  # type: ignore

from file_manager_py_package.memory_manager import MemoryManager
# csv_manager, file_manager
WELCOME_MESSAGE = "Welcome to the File Manager for Python!"


def import_files_and_clear_data(option: str):
    """Handle importing files and clearing data based on option."""
    ic = InputController()
    mm = MemoryManager()
    if option == "import":
        response = ic.format_bool("Do you want to import files "
                                  "into the application? (yes/no): ")
        if response:
            print("You chose to import files.")
            mm.copy_files_from_directory()
        else:
            print("You chose not to import files.")

    elif option == "clear":
        response = ic.format_bool("Do you want to clear "
                                  "the application data? (yes/no): ")
        if response:
            print("You chose to clear the application data.")
            mm.clear_app_data()
        else:
            print("You chose not to clear the application data.")


def display_welcome_message():
    """Display the welcome message."""
    print(WELCOME_MESSAGE)
