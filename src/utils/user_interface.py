"""User interface utilities for the application."""
import subprocess
import time
from src.utils import os_check


class UserInterface:
    """A class to handle user interactions and display messages."""
    prompt = ">>> "  # Default prompt for user input

    @staticmethod
    def display_message(message: str) -> None:
        """Display a message to the user."""
        print(message)

    @staticmethod
    def get_user_input(prompt: str) -> str:
        """Get input from the user."""
        return input(prompt)

    @staticmethod
    def show_app_info(version: str, author: str, lic: str = "") -> None:
        """Displays information about the application."""
        print(f"""
+----------------------------------------------------------+
|Welcome to the File Handler for Python!                   |
+----------------------------------------------------------+
|This application allows you to manage files and databases.|
|Version: {version}                                            |
|Author: {author}                                |
|License: {lic}                                      |
+==========================================================+
          """)

    @staticmethod
    def wait_time(seconds: int = 1) -> None:
        """Wait for a specified number of seconds."""
        time.sleep(seconds)

    @staticmethod
    def clear_console(opt: int = 0) -> None:
        """Clear the console screen."""
        if opt == 0:  # Clear the console screen based on the operating system
            os_type = os_check.OpereatingSystem()
            if os_type.is_windows():
                subprocess.run("cls", shell=True, check=False)
            else:
                subprocess.run("clear", shell=True, check=False)
        else:
            # Clear the console screen using ANSI escape codes
            print("\033[H\033[J", end="")

    @staticmethod
    def wait_and_clear_console(seconds: int = 1, opt: int = 0) -> None:
        """Waits for a specified number of seconds and
        then clears the console."""
        UserInterface.wait_time(seconds)
        UserInterface.clear_console(opt)


def main():
    """Main function to demonstrate the user interface."""
    ui = UserInterface()
    ui.display_message("Welcome to the application!")
    name = ui.get_user_input("Please enter your name: ")
    ui.display_message(f"Hello, {name}! Nice to meet you.")
    ui.wait_time(2)
    ui.display_message("Clearing the console in 3 seconds...")
    ui.wait_time(3)
    ui.clear_console()
    ui.display_message("Console cleared. Goodbye!")


if __name__ == "__main__":
    main()
