"""The main entry point for the application."""
import utils.start_end as se


def main():
    """The main function."""
    se.display_welcome_message()
    while True:
        se.import_files_and_clear_data(option="import")
        #
        #
        #
        # Here you can add more functionality or
        # options for the user to interact with the application.
        #
        #
        #
        #
        # Here you can add more functionality or
        # options for the user to interact with the application.
        #
        #
        #
        se.import_files_and_clear_data(option="clear")
        # Break if exit is typed, otherwise continue the loop
        exit_response = input("Type 'exit' to quit or press \
                              Enter to continue: ")
        if exit_response.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break

        print("Continuing the application...")


if __name__ == "__main__":
    main()
