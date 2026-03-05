"""File handler package for Python."""
import os

ENCODING_STR = "utf-8"


class FileHandler:
    """A simple file handler class."""
    def __init__(self, file_path: str, encoding: str = ENCODING_STR) -> None:
        self.file_path = file_path
        self.encoding = encoding

    def exists_file_at(self, path: str) -> bool:
        """Check if a file exists at the specified path."""
        return os.path.isfile(path)

    def identify_file_type(self) -> str:
        """Identify the file type based on its extension."""
        _, ext = os.path.splitext(self.file_path)
        return ext.lower()

    def read(self) -> str:
        """Read the contents of the file."""
        if not self.exists_file_at(self.file_path):
            raise FileNotFoundError(f"No file found at {self.file_path}")
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            return file.read()

    def write(self, content: str) -> None:
        """Write content to the file, overwriting any existing content."""
        with open(self.file_path, 'w', encoding=self.encoding) as file:
            file.write(content)

    def append(self, content: str) -> None:
        """Append content to the end of the file."""
        with open(self.file_path, 'a', encoding=self.encoding) as file:
            file.write(content)

    def delete(self, path: str) -> None:
        """Delete the file."""
        p = path
        if self.exists_file_at(p):
            os.remove(p)
        else:
            raise FileNotFoundError(f"No file found at {p}")
