"""Data Base Management System"""
import os
import sqlite3


class DataBaseManager:
    """Data Base Management System"""

    def __init__(self, db_name: str = "file_manager.db"):
        self.db_name = db_name
        self.connection: sqlite3.Connection | None = None
        self.cursor: sqlite3.Cursor | None = None
        self._connect()
        self._create_table()

    def _connect(self) -> None:
        """Connect to the SQLite database."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def _require_cursor(self) -> sqlite3.Cursor:
        if self.cursor is None:
            raise RuntimeError("Database cursor is not initialized.")
        return self.cursor

    def _require_connection(self) -> sqlite3.Connection:
        if self.connection is None:
            raise RuntimeError("Database connection is not initialized.")
        return self.connection

    def _create_table(self) -> None:
        """Create the files table if it doesn't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT NOT NULL,
            file_size INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor = self._require_cursor()
        connection = self._require_connection()
        cursor.execute(create_table_query)
        connection.commit()

    def add_file(self, file_path: str) -> None:
        """Add a file record to the database."""
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")

        file_size = os.path.getsize(file_path)
        insert_query = "INSERT INTO files (file_path, file_size) VALUES (?, ?)"
        cursor = self._require_cursor()
        connection = self._require_connection()
        cursor.execute(insert_query, (file_path, file_size))
        connection.commit()

    def get_all_files(self) -> list[tuple]:
        """Retrieve all file records from the database."""
        cursor = self._require_cursor()
        cursor.execute("SELECT * FROM files")
        return cursor.fetchall()

    def close(self) -> None:
        """Close the database connection."""
        if self.connection is not None:
            self.connection.close()


def initialize_database(db_file, sql_script):
    """Initialize the database by executing the SQL script."""
    try:
        # 1. Connect to the database file
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 2. Read the SQL script
        with open(sql_script, 'r', encoding='utf-8') as f:
            sql_as_string = f.read()

        # 3. Execute the script (executes multiple statements at once)
        cursor.executescript(sql_as_string)

        print("Tables created successfully.")
        conn.commit()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

# Usage: initialize_database('my_data.db', 'DATABASE.sql')
