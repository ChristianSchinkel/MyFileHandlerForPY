"""
File Manager for handling file operations
such as saving and loading data.
"""
import os
import shutil


class FileManager:
    """
    A class to manage file operations such as saving and loading data.
    """
    encoder = "utf-8"
    app_data_dir = "app_data"

    def __init__(self,
                 directory: str = "app_data",
                 encoder: str = "utf-8") -> None:
        """Initializes the FileManager and ensures the app data
        directory exists."""
        if not os.path.exists(self.app_data_dir):
            os.makedirs(self.app_data_dir)
        self.directory = directory
        self.encoder = encoder

    def count_number_of_files_in_directory(self, directory: str) -> int:
        """Counts the number of files in the specified directory."""
        try:
            return len([f for f in os.listdir(directory)
                        if os.path.isfile(os.path.join(directory, f))])
        except FileNotFoundError:
            print(f"Directory '{directory}' does not exist.")
        return 0

    # Count same file name and extension in the directory and return the count
    def count_files_with_name_and_extension(self, directory: str,
                                            name: str,
                                            extension: str) -> int:
        """Counts the number of files in the specified directory
        with the given name and extension."""
        try:
            return len([f for f in os.listdir(directory)
                        if os.path.isfile(os.path.join(directory, f))
                        and f.startswith(name) and f.endswith(extension)])
        except FileNotFoundError:
            print(f"Directory '{directory}' does not exist.")
        return 0

    def exist(self, file_name: str) -> bool:
        """Checks if a file with the given name exists."""
        try:
            with open(file_name, 'r', encoding=self.encoder):
                return True
        except FileNotFoundError:
            return False

    def create_file(self, file_name: str) -> None:
        """Creates a file with the given name."""
        if self.exist(file_name):
            print(f"File '{file_name}' already exists.")

        with open(file_name, 'w', encoding=self.encoder) as file:
            file.write("")  # Create an empty file
        print(f"File '{file_name}' created successfully.")

    def read_file(self, file_name: str) -> str:
        """Reads the content of the file with the given name and returns it."""
        try:
            with open(file_name, 'r', encoding=self.encoder) as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{file_name}' does not exist.")
        return ""

    def update_file(self, file_name: str, data: str) -> None:
        """Updates the file with the given name by writing the provided data.
        """
        if not self.exist(file_name):
            print(f"File '{file_name}' does not exist. Creating a new file.")
            self.create_file(file_name)
        with open(file_name, 'w', encoding=self.encoder) as file:
            file.write(data)
        print(f"File '{file_name}' updated successfully.")

    # Imprt file from a directory to a target directory
    def import_file_from_directory(self, directory: str,
                                   target_directory: str) -> None:
        """Imports a file from the specified directory to the target directory.
        """
        if not os.path.exists(directory):
            print(f"Directory '{directory}' does not exist.")
            return
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
            # Copy file with name "UserDefaults.txt" from directory
            # to target_directory
        source_file = os.path.join(directory, "UserDefaults.txt")
        target_file = os.path.join(target_directory, "UserDefaults.txt")
        if os.path.isfile(source_file):
            shutil.copy(source_file, target_file)
            print(f"File 'UserDefaults.txt' imported successfully to "
                  f"'{target_directory}'.")
        else:
            print(f"File 'UserDefaults.txt' does not exist in '{directory}'.")

    def import_files_from_directory(self, directory: str,
                                    target_directory: str) -> None:
        """Imports files from the specified directory to the target directory.
        """
        if not os.path.exists(directory):
            print(f"Directory '{directory}' does not exist.")
            return
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        for file_name in os.listdir(directory):
            sp = os.path.join(directory, file_name)
            tp = os.path.join(target_directory, file_name)
            if os.path.isfile(sp):
                with open(sp, 'r', encoding=self.encoder) as source_file:
                    data = source_file.read()
                with open(tp, 'w', encoding=self.encoder) as target_file:
                    target_file.write(data)
                print(f"File '{file_name}' imported "
                      f"successfully to '{target_directory}'.")

    def delete_file(self, file_name: str) -> None:
        """Deletes the file with the given name."""

        if not self.exist(file_name):
            print(f"File '{file_name}' does not exist.")
            return

        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")

    def delete_files_in_directory(self, directory: str) -> None:
        """Deletes all files in the specified directory."""
        if not os.path.exists(directory):
            print(f"Directory '{directory}' does not exist.")
            return

        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File '{file_name}' deleted successfully from "
                      f"'{directory}'.")

    def construct_file_name(self, name: str, extension: str) -> str:
        """Constructs a file name with the given name and extension."""
        return f"{name}.{extension}"

    def get_file_name(self) -> str:
        """Prompts the user to enter a file name and returns it."""
        fn = input("Enter the file name: ")
        return fn


def main() -> None:
    """The main function."""


if __name__ == "__main__":
    main()
