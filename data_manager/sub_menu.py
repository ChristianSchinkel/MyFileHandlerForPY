"""Sub-menu for data management operations."""
from data_manager.file_manager import FileManager
from data_manager.database_managment_system import DatabaseManagementSystem


def display_file_handler_menu(fm: FileManager):
    """Displays the file handler menu and handles user input."""
    is_running = True
    while is_running:
        print("""File Handler Menu:\n
1. Create File\n
2. Read File\n
2.2 Import File\n
3. Update File\n
4. Delete File\n
5. Back to Main Menu
          """)
        choice = input("Please select an option: ")
        if choice == "1":
            # Import the file creation function and call it
            fm.create_file("example.txt")
        elif choice == "2":
            # Import the file reading function and call it
            fm.read_file("example.txt")
        elif choice == "2.2":
            # Import the file import function and call it
            fm.import_files_from_directory("example.txt", "target_directory")
        elif choice == "3":
            # Import the file update function and call it
            fm.update_file("example.txt", "This is some updated content.")
        elif choice == "4":
            # Import the file deletion function and call it
            fm.delete_file("example.txt")
        elif choice == "5":
            print("Returning to the main menu.")
            is_running = False
        else:
            print("Invalid choice. Please try again.")


def display_database_handler_menu(dbms: DatabaseManagementSystem):
    """Displays the database handler menu and handles user input."""
    is_running = True
    while is_running:
        print("""Database Handler Menu:\n
1. Create Record\n
2. Read Record\n
3. Update Record\n
4. Delete Record\n
5. Back to Main Menu
          """)
        choice = input("Please select an option: ")
        if choice == "1":
            # Import the record creation function and call it

            # Cheate  a schema
            tn = input("Enter the name of the table to create: ")
            fields = ((),)
            schema = dbms.DataBaseSchema(tn, fields)
            schema.create_table_name()
            schema.create_columns()
            dbms.create_table(schema)

            # Create Record from schema
            dbms.create_table(schema)

        elif choice == "2":
            # Import the record reading function and call it
            print("Read Record functionality is not implemented yet.")
        elif choice == "3":
            # Import the record update function and call it
            print("Update Record functionality is not implemented yet.")
        elif choice == "4":
            # Import the record deletion function and call it
            print("Delete Record functionality is not implemented yet.")
        elif choice == "5":
            print("Returning to the main menu.")
            is_running = False
        else:
            print("Invalid choice. Please try again.")


def main() -> None:
    """The main function for the data management sub-menu."""
    print("Data Management Sub-Menu is not implemented yet.")


if __name__ == "__main__":
    main()
