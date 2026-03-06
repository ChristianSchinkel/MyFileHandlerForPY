"""""Directory Manager for Python."""
import os


class DirectoryManager:
    """A simple directory manager class."""
    def __init__(self, directory_path: str) -> None:
        self.directory_path = directory_path

    def set_directory_path(self, path: str) -> None:
        """Set the directory path."""
        self.directory_path = path

    def exists_directory_at(self, path: str) -> bool:
        """Check if a directory exists at the specified path."""
        return os.path.isdir(path)

    def get_directory_contents(self) -> list:
        """Get the contents of the directory."""
        if not self.exists_directory_at(self.directory_path):
            raise FileNotFoundError(f"No directory "
                                    f"found at {self.directory_path}")
        return os.listdir(self.directory_path)
