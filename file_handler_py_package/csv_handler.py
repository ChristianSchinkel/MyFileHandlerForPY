"""CSV handler for Python."""
import csv
from typing import Any, Dict, List, Optional
from file_handler_py_package.file_handler import ENCODING_STR
from .file_handler import FileHandler

DELIMITER_STR = ','


class CSVHandler(FileHandler):
    """A CSV file handler class."""
    def __init__(self,
                 file_path: str,
                 delimiter: str = DELIMITER_STR,
                 encoding: str = ENCODING_STR) -> None:
        super().__init__(file_path, encoding)
        self.delimiter = delimiter

    def read_csv(self, path: str) -> List[Dict[str, str]]:
        """Read the contents of the CSV file and return a list of
        dictionaries.
        """
        if self.exists_file_at(path):
            with open(path, 'r', encoding=self.encoding) as file:
                reader = csv.DictReader(file, delimiter=self.delimiter)
                return list(reader)
        else:
            raise FileNotFoundError("File not found")

    def write_csv(self,
                  data: List[Dict[str, Any]],
                  fieldnames: Optional[List[str]] = None) -> None:
        """Write a list of dictionaries to the CSV file."""
        if not data and not fieldnames:
            raise ValueError("Must provide either \
                             data or fieldnames to write.")

        # Infer fieldnames from data the first row if not provided
        keys = fieldnames if fieldnames else list(data[0].keys())

        with open(self.file_path,
                  'w',
                  encoding=self.encoding,
                  newline='') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=keys,
                                    delimiter=self.delimiter)
            writer.writeheader()
            writer.writerows(data)

    def append_row(self, row: Dict[str, Any]) -> None:
        """Append a single row to the CSV file."""
        with open(self.file_path,
                  'a',
                  encoding=self.encoding,
                  newline='') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=row.keys(),
                                    delimiter=self.delimiter)
            if file.tell() == 0:  # Check if file is empty
                writer.writeheader()
            writer.writerow(row)
