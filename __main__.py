"""The main entry point for the application."""
from InputController.inputController import InputController  # type: ignore

from file_manager_py_package.memory_manager import MemoryManager
# csv_manager, file_manager
WELCOME_MESSAGE = "Welcome to the File Manager for Python!"


def main():
    """The main function."""
    display_welcome_message()
    while True:
        import_files_and_clear_data(option="import")
        #
        #
        #
        # Here you can add more functionality or
        # options for the user to interact with the application.
        #
        #
        #
        #
        # Here you can add more functionality or
        # options for the user to interact with the application.
        #
        #
        #
        import_files_and_clear_data(option="clear")
        # Break if exit is typed, otherwise continue the loop
        exit_response = input("Type 'exit' to quit or press \
                              Enter to continue: ")
        if exit_response.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break

        print("Continuing the application...")


def import_files_and_clear_data(option: str):
    """Handle importing files and clearing data based on option."""
    ic = InputController()
    mm = MemoryManager()
    if option == "import":
        response = ic.format_bool("Do you want to import files \
                   into the application? (yes/no): ")
        if response:
            print("You chose to import files.")
            mm.copy_files_from_directory()
        else:
            print("You chose not to import files.")

    elif option == "clear":
        response = ic.format_bool("Do you want to clear \
                        the application data? (yes/no): ")
        if response:
            print("You chose to clear the application data.")
            mm.clear_app_data()
        else:
            print("You chose not to clear the application data.")


def display_welcome_message():
    """Display the welcome message."""
    print(WELCOME_MESSAGE)


if __name__ == "__main__":
    main()
