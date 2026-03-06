"""The main entry point for the application."""
import os
from time import sleep

from file_manager_py_package.memory_manager import MemoryManager
# csv_manager, file_manager
WELCOME_MESSAGE = "Welcome to the File Manager for Python!"


def main():
    """The main function."""
    print(WELCOME_MESSAGE)
    # fh = file_manager.FileManager("app_data/test.txt")
    # ch = csv_manager.CSVManager("app_data/test.csv")
    mm = MemoryManager()
    print(mm.directory_manager)
    mm.copy_files_from_directory()
    # Wait for 5 seconds before proceeding
    print("Waiting for 5 seconds...")
    sleep(2)

    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    mm.clear_app_data()
    # fh.write("This is a test file.")
    # ch.write_csv([{"name": "John", "age": 30},
    #               {"name": "Jane", "age": 25}])


if __name__ == "__main__":
    main()
