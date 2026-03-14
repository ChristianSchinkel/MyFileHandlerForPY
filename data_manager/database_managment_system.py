"""Database Management System for handling database operations."""
import sqlite3
import file_manager
# import InputController

count = file_manager.count_files_with_name_and_extension('.',
                                                         'Database',
                                                         '.db')


class DatabaseManagementSystem:
    """
    A class to manage database operations such as creating, reading,
    updating, and deleting databases.
    """
    def __init__(self, db_name: str = f"Database{count}.db"):
        self.db_name = db_name
        self.connection = None


def main() -> None:
    """Main function for Database Management System."""
    dbms = DatabaseManagementSystem()
    # Example usage of the DatabaseManagementSystem class
    print("This is the Database Management System Module.")
    connection = sqlite3.connect(dbms.db_name)
    # Create a list of table containing strings
    table_names = []
    table_name = input("Enter the name of the table to create: ")
    table_names.append(table_name)
    # Create a table in the database
    connection.execute(f'''
CREATE TABLE IF NOT EXISTS {table_name.lower()} (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
                       ''')
    # Write the table names to a file
    connection.commit()
    # Close the connection to the database
    connection.close()
    # Create a sample table

    # Insert sample data into the table


if __name__ == "__main__":
    main()
