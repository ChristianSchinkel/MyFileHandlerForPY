"""
File Manager for handling file operations
such as saving and loading data.
"""
import os


ENCODING = 'utf-8'


class FileManager:
    """
    A class to manage file operations such as saving and loading data.
    """
    pass


def count_number_of_files_in_directory(directory: str) -> int:
    """Counts the number of files in the specified directory."""
    try:
        return len([f for f in os.listdir(directory)
                    if os.path.isfile(os.path.join(directory, f))])
    except FileNotFoundError:
        print(f"Directory '{directory}' does not exist.")
        return 0


# Cound same file name and extension in the directory and return the count
def count_files_with_name_and_extension(
        directory: str,
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


def exist(file_name: str) -> bool:
    """Checks if a file with the given name exists."""
    try:
        with open(file_name, 'r', encoding=ENCODING):
            return True
    except FileNotFoundError:
        return False


def create_file(file_name: str) -> None:
    """Creates a file with the given name."""
    if exist(file_name):
        print(f"File '{file_name}' already exists.")
        return

    with open(file_name, 'w', encoding=ENCODING) as file:
        file.write("")  # Create an empty file
        print(f"File '{file_name}' created successfully.")


def read_file(file_name: str) -> str:
    """Reads the content of the file with the given name and returns it."""
    try:
        with open(file_name, 'r', encoding=ENCODING) as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")
        return ""


def update_file(file_name: str, data: str) -> None:
    """Updates the file with the given name by writing the provided data."""
    if not exist(file_name):
        print(f"File '{file_name}' does not exist. Creating a new file.")
        create_file(file_name)

    with open(file_name, 'w', encoding=ENCODING) as file:
        file.write(data)
        print(f"File '{file_name}' updated successfully.")


def delete_file(file_name: str) -> None:
    """Deletes the file with the given name."""

    if not exist(file_name):
        print(f"File '{file_name}' does not exist.")
        return

    os.remove(file_name)
    print(f"File '{file_name}' deleted successfully.")


def construct_file_name(name: str, extension: str) -> str:
    """Constructs a file name with the given name and extension."""
    return f"{name}.{extension}"


def get_file_name() -> str:
    """Prompts the user to enter a file name and returns it."""
    fn = input("Enter the file name: ")

    return fn


def main() -> None:
    """The main function."""
    pass


if __name__ == "__main__":
    main()
