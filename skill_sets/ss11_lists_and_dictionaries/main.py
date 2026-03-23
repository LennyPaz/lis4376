#!/usr/bin/env python3
"""SS11 - Lists and Dictionaries with Data Validation"""
import functions as f


def main():
    """main function for lists and dictionaries program"""
    # initialize variable(s)
    your_emails = []
    your_phones = []
    your_firstname = []
    your_lastname = []
    your_dictionary = {}

    # function calls
    f.get_requirements()
    your_emails = f.add_emails()

    if len(your_emails) == 0:
        print("No emails!")
    else:
        your_phones = f.get_phones(your_emails)
        your_firstname, your_lastname = f.get_names(your_emails)
        your_dictionary = f.create_contact(your_emails, your_phones,
                                           your_firstname, your_lastname)

    # menu-driven loop
    while True:
        f.get_menu()
        command = f.get_command()

        if command.upper() != "Q":
            f.run_command(command, your_dictionary)
        else:
            print("\nEnding program!\n")
            break


if __name__ == "__main__":
    main()
