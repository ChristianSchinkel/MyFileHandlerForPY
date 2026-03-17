"""Database Management System for handling database operations."""
import sqlite3
from src.data_manager.file_manager import FileManager
# import InputController

fm = FileManager()
count = fm.count_files_with_name_and_extension('.', 'Database', '.db')
DEFAULT_PATH = f"./app_data/persistance/Database{count}.db"


class DatabaseManagementSystem:
    """
    A class to manage database operations such as creating, reading,
    updating, and deleting databases.
    """
    def __init__(self, db_name: str = DEFAULT_PATH):
        self.db_name = db_name
        self.connection = None

    class DataBaseSchema:
        """A class to define the database schema."""
        def __init__(self, table_name: str, columns: tuple):
            self.table_name = table_name
            self.columns = columns

        def create_table_name(self) -> str:
            """Create a table name based on the provided table name."""
            user_input = input("Enter the name of the table to create: ")
            self.table_name = user_input
            return self.table_name.lower()

        def create_columns(self) -> str:
            """Create a string of columns for creation of the table fields.
            The user is prompted to enter the columns and their data types.
            """
            user_input = input("""Enter the columns and their data types
                               (e.g., 'title TEXT, year INTEGER'): """)
            pair = user_input.split(',')
            pair = [item.strip() for item in pair]
            self.columns = tuple(pair)
            return ', '.join(self.columns)

    def create_connection(self) -> sqlite3.Connection:
        """Create a connection to the database."""
        return sqlite3.connect(self.db_name)

    def create_curesor(self) -> sqlite3.Cursor:
        """Create a cursor object to execute SQL commands."""
        con = self.create_connection()
        return con.cursor()

    def create_table(self, schema: DataBaseSchema) -> None:
        """Create a table in the database based on the provided schema."""
        con = self.create_connection()
        cur = self.create_curesor()
        cur.execute(f'''
                    CREATE TABLE IF NOT EXISTS {schema.create_table_name()} (
                    id INTEGER PRIMARY KEY,
                    {schema.create_columns()}
                    )''')
        con.commit()
        con.close()

    def result_exists(self, table_name: str) -> bool:
        """Check if a result exists for a given query."""
        con = self.create_connection()
        cur = self.create_curesor()
        query = f"""SELECT {table_name} FROM sqlite_master"""
        res = cur.execute(query)
        exists = res.fetchone() is not None
        print(f"Result exists for query '{query}': {exists}")
        con.close()
        return exists

    def insert_data(self, table_name: str, data: list) -> None:
        """Insert data into the specified table."""
        con = self.create_connection()
        cur = self.create_curesor()
        placeholders = ', '.join(['?'] * len(data[0]))
        query = f"INSERT INTO {table_name} VALUES({placeholders})"
        cur.executemany(query, data)
        con.commit()
        con.close()

    def insert_many_data(self, table_name: str, data: list) -> None:
        """Insert many rows of data into the specified table."""
        con = self.create_connection()
        cur = self.create_curesor()
        placeholders = ', '.join(['?'] * len(data[0]))
        query = f"INSERT INTO {table_name} VALUES({placeholders})"
        cur.executemany(query, data)
        con.commit()
        con.close()

    def print_conttents(self, table_name: str) -> None:
        """Print the contents of the specified table."""
        con = self.create_connection()
        cur = self.create_curesor()
        query = f"SELECT * FROM {table_name}"
        for row in cur.execute(query):
            print(row)
        con.close()


def main() -> None:
    """Main function for Database Management System."""
    dbms = DatabaseManagementSystem()
    # Example usage of the DatabaseManagementSystem class
    print("This is the Database Management System Module.")
    con = sqlite3.connect(dbms.db_name)
    # Create a list of table containing strings
    table_names = []
    table_name = input("Enter the name of the table to create: ")
    table_names.append(table_name)
    # Create Cursor object to execute SQL commands
    cur = con.cursor()
    # Create a table in the database
    cur.execute(f'''
CREATE TABLE IF NOT EXISTS {table_name.lower()} (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    score REAL NOT NULL
)
                       ''')
    # Check if the table was created successfully
    res = cur.execute('''SELECT name FROM sqlite_master''')
    res.fetchone()
    # Return Boolean if a table is not existing.
    res = cur.execute("""SELECT name FROM sqlite_master WHERE name='spam'""")
    print(res.fetchone() is None)
    # Insert data into the table
    cur.execute(f"""
        INSERT INTO {table_name.lower()} VALUES
            ('1', 'Monty Python and the Holy Grail', 1975, 8.2),
            ('2', 'And Now for Something Completely Different', 1971, 7.5)
                """)
    con.commit()
    # Query the table to retrieve data
    res = cur.execute("SELECT score FROM movie")
    res.fetchall()

    # Insert sample data into the table
    data = [
        ("3", "Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("4", "Monty Python's The Meaning of Life", 1983, 7.5),
        ("5", "Monty Python's Life of Brian", 1979, 8.0),
    ]
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?, ?)", data)
    # Notice that ? placeholders are used to bind data to the query.
    # Always use placeholders instead of string formatting
    # to bind Python values to SQL statements,
    # to avoid SQL injection attacks (see How to use placeholders
    # to bind values in SQL queries for more details).
    con.commit()  # Remember to commit the transaction after executing INSERT.
    # Print the data in the table
    for row in cur.execute("""
                           SELECT year, title FROM movie ORDER BY year
                           """):
        print(row)

    # Close the connection to the database
    con.close()
    # Create a new connection to the database and query the data
    new_con = sqlite3.connect(DatabaseManagementSystem().db_name)
    new_cur = new_con.cursor()
    res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
    title, year = res.fetchone()
    print(f"""The highest scoring Monty Python movie is {title!r},
          released in {year}""")
    new_con.close()


if __name__ == "__main__":
    main()
