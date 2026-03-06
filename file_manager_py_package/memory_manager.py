"""Memory Manager for Python."""
import os
import shutil
from .directory_manager import DirectoryManager
from .file_manager import FileManager


class MemoryManager:
    """Memory manager handles the logic for Storage Files."""
    ROOT_DIRECTORY = "./app_data"
    directory_manager = DirectoryManager(ROOT_DIRECTORY)
    file_manager = FileManager(f"{ROOT_DIRECTORY}/storage.txt")

    def __init__(self) -> None:
        if self.directory_manager.exists_directory_at(self.ROOT_DIRECTORY):
            print(f"Directory {self.ROOT_DIRECTORY} exists.")
        else:
            print(f"Directory {self.ROOT_DIRECTORY} does not exist.")

    def get_memory(self) -> str:
        """Get the memory from the storage file."""
        return self.file_manager.read()

    def set_memory(self, content: str) -> None:
        """Set the memory in the storage file."""
        self.file_manager.write(content)

    def ask_for_path(self, path: str) -> str:
        """Ask for a path and set it as the memory."""
        path = input("Please enter a path: ")
        return path

    def copy_files_from_directory(self) -> None:
        """Copy Content of the directory from source to destination."""
        source = self.ask_for_path("Please enter the source path: ")
        destination = self.directory_manager.directory_path
        if not os.path.isdir(source):
            raise FileNotFoundError(f"No directory found at {source}")
        for filename in os.listdir(source):
            src_file = os.path.join(source, filename)
            dst_file = os.path.join(destination, filename)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dst_file)
                print(f"Imported {src_file} from {source} "
                      f"to {dst_file} in {destination}")
        print(f"Files copied from {source} to {destination}")

    def clear_app_data(self) -> None:
        """Clear all data in the application directory."""
        for filename in os.listdir(self.ROOT_DIRECTORY):
            file_path = os.path.join(self.ROOT_DIRECTORY, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print(f"Application data cleared from {self.ROOT_DIRECTORY}")
