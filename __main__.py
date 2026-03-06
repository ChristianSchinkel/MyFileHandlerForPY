"""The main entry point for the application."""
from file_manager_py_package import csv_manager, file_manager


def main():
    """The main function."""
    print("Hello, World!")
    fh = file_manager.FileManager("app_data/test.txt")
    ch = csv_manager.CSVManager("app_data/test.csv")
    fh.write("This is a test file.")
    ch.write_csv([{"name": "John", "age": 30},
                  {"name": "Jane", "age": 25}])


if __name__ == "__main__":
    main()
