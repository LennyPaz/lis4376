#!/usr/bin/env python3
"""SS11 - Functions for Lists and Dictionaries

Defines eleven functions:

1. get_requirements()
2. add_emails()
3. get_phones()
4. get_names()
5. create_contact()
6. get_menu()
7. get_command()
8. run_command()
9. list_contacts()
10. remove_contact()
11. update_contact()
"""

COMMANDS = ('U', 'D', 'L', 'Q')
MENU = """\nMenu:
U - Update contact
D - Delete contact
L - List contacts
Q - Quit"""


def get_requirements():
    """prints developer info and program requirements"""
    print("\nDeveloper: Lenny Paz")
    print("Working with lists, dictionaries, and user-entered values.")
    print("\nProgram Requirements:\n"
          + "1. Write a program that prints all elements of a user-entered contact list.\n"
          + "2. Must perform data validation.\n"
          + "3. Dictionary key: user's email address.\n"
          + "4. Dictionary value: user's phone number.\n")

    print("***Extra credit (10 pts):***\n"
          + "a. Provide additional functionality to add contacts' first and last names (10 pts).\n"
          + "b. Provide additional functionality to update and/or delete contacts (10 pts). Both required.\n")

    print("***Resource(s):***\n"
          + "Python dictionaries: https://www.w3schools.com/python/python_dictionaries.asp\n"
          + "  https://docs.python.org/3/tutorial/datastructures.html#dictionaries\n")

    print("Input:\n"
          + "Enter -1 to stop adding e-mails.\n")


def add_emails():
    """prompts for email addresses with validation, returns list"""
    your_emails = []
    counter = 1

    while True:
        try:
            email = input("Enter e-mail " + str(counter) + ": ")

            if email.strip()[0:1] == "":
                raise IndexError

            if email.strip() == "-1":
                break

            your_emails.append(email.strip())
            counter += 1

        except IndexError:
            print("No e-mail entered! Try again.\n")

    return your_emails


def get_phones(emails_list):
    """prompts for phone number for each email, returns list"""
    your_phones = []

    for i in range(len(emails_list)):
        while True:
            try:
                phone = input("Enter phone for " + emails_list[i] + ": ")

                if phone.strip()[0:1] == "":
                    raise IndexError

                your_phones.append(phone.strip())
                break

            except IndexError:
                print("No phone entered! Try again.\n")

    return your_phones


def get_names(emails_list):
    """prompts for first and last name for each email, returns two lists"""
    your_firstname = []
    your_lastname = []

    for i in range(len(emails_list)):
        # get first name
        while True:
            try:
                first = input("Enter first name for " + emails_list[i] + ": ")

                if first.strip()[0:1] == "":
                    raise IndexError

                your_firstname.append(first.strip())
                break

            except IndexError:
                print("No first name entered! Try again.\n")

        # get last name
        while True:
            try:
                last = input("Enter last name for " + emails_list[i] + ": ")

                if last.strip()[0:1] == "":
                    raise IndexError

                your_lastname.append(last.strip())
                break

            except IndexError:
                print("No last name entered! Try again.\n")

    return your_firstname, your_lastname


def create_contact(keys, values, values2, values3):
    """creates dictionary from lists using zip, displays and returns it"""
    my_dictionary = dict(zip(keys, zip(values, values2, values3)))

    print("\nPrinting dictionary:\n", my_dictionary)
    print("\nPrinting keys:\n", my_dictionary.keys())
    print("\nPrinting values:\n", my_dictionary.values())
    print("\nPrinting items:\n", my_dictionary.items())

    return my_dictionary


def get_menu():
    """displays the menu options"""
    print(MENU)


def get_command():
    """prompts for and validates menu command, returns uppercase string"""
    while True:
        command = input("\nEnter command: ").strip().upper()

        if command in COMMANDS:
            return command
        else:
            print("Invalid command! Try again.")


def run_command(command, my_dictionary):
    """routes command to the appropriate function"""
    if command == "U":
        update_contact(my_dictionary)
    elif command == "D":
        remove_contact(my_dictionary)
    elif command == "L":
        list_contacts(my_dictionary)


def list_contacts(my_dictionary):
    """displays all contacts in the dictionary"""
    print("\nPrinting dictionary:\n", my_dictionary)
    print("\nPrinting keys:\n", my_dictionary.keys())
    print("\nPrinting values:\n", my_dictionary.values())
    print("\nPrinting items:\n", my_dictionary.items())


def remove_contact(my_dictionary):
    """lists contacts by index, prompts for selection, and deletes contact"""
    if len(my_dictionary) == 0:
        print("No contacts to delete!")
        return

    contact_list = list(my_dictionary.keys())

    print("\nContacts:")
    for i in range(len(contact_list)):
        print(str(i) + ": " + contact_list[i])

    while True:
        try:
            del_contact = input("\nEnter contact number to delete (-1 to quit): ")

            if del_contact.strip() == "-1":
                break

            del_contact = int(del_contact)

            if del_contact < 0 or del_contact > len(contact_list) - 1:
                print("Number must be between 0 and " + str(len(contact_list) - 1) + ".")
                continue

            del my_dictionary[contact_list[del_contact]]
            print("Contact deleted!")
            break

        except ValueError:
            print("Not an int! Try again.\n")


def update_contact(my_dictionary):
    """lists contacts by index, prompts for new values, and updates contact"""
    if len(my_dictionary) == 0:
        print("No contacts to update!")
        return

    contact_list = list(my_dictionary.keys())

    print("\nContacts:")
    for i in range(len(contact_list)):
        print(str(i) + ": " + contact_list[i])

    while True:
        try:
            upd_contact = input("\nEnter contact number to update (-1 to quit): ")

            if upd_contact.strip() == "-1":
                break

            upd_contact = int(upd_contact)

            if upd_contact < 0 or upd_contact > len(contact_list) - 1:
                print("Number must be between 0 and " + str(len(contact_list) - 1) + ".")
                continue

            key = contact_list[upd_contact]
            phone = input("Enter new phone number: ")
            first = input("Enter new first name: ")
            last = input("Enter new last name: ")

            my_dictionary.update({key: (phone, first, last)})
            print("Contact updated!")
            break

        except ValueError:
            print("Not an int! Try again.\n")
