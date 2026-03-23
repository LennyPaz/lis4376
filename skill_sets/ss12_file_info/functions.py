#!/usr/bin/env python3
"""SS12 - Functions for File Info

Defines ten functions:

1. get_requirements()
2. get_menu()
3. get_command()
4. run_command()
5. list_dir()
6. move_up()
7. move_down()
8. num_files()
9. num_bytes()
10. find_files()
"""
import os
import os.path

COMMANDS = ('1', '2', '3', '4', '5', '6', '7')
MENU = """\nMENU:
1 List
2 Up
3 Down
4 Count
5 Size
6 Search
7 Quit"""


def get_requirements():
    """prints developer info and program requirements"""
    print("\nDeveloper: Lenny Paz")
    print("Program navigates file system to locate and display file system information.\n")
    print("Program Requirements:\n"
          + "1. Write program functions that navigate and display file system information.\n"
          + "2. Create interactive menu for user.\n"
          + "3. Must prevent incorrect command input.\n")

    print("***Resource(s):***\n"
          + "Python os package: https://docs.python.org/3/library/os.html\n")


def get_menu():
    """displays current working directory and menu options"""
    print("\nCurrent working directory:\n" + os.getcwd())
    print(MENU)


def get_command():
    """prompts for and validates menu command, returns string"""
    while True:
        command = input("\nEnter command: ").strip()

        if command in COMMANDS:
            return command
        else:
            print("Invalid command! Try again.")


def run_command(command):
    """routes command to the appropriate function"""
    cur_dir = os.getcwd()

    if command == "1":
        list_dir(cur_dir)
    elif command == "2":
        move_up()
    elif command == "3":
        move_down(cur_dir)
    elif command == "4":
        count = num_files(cur_dir)
        print("\n{0}{1: ,d}".format("Files: ", count))
    elif command == "5":
        total = num_bytes(cur_dir)
        print("\n{0}{1: ,d} bytes".format("Size: ", total))
        print("{0}{1: ,.2f} KB".format("Size: ", total / 1000))
        print("{0}{1: ,.2f} MB".format("Size: ", total / 1000000))
        print("{0}{1: ,.2f} GB".format("Size: ", total / 1000000000))
    elif command == "6":
        my_file = input("\nEnter file name to search: ")
        results = find_files(my_file, cur_dir)

        if len(results) == 0:
            print("\nNo files found.")
        else:
            print("\nFiles found:")
            for f in results:
                print(f)


def list_dir(dir_name):
    """lists all files and directories in the given directory"""
    for element in os.listdir(dir_name):
        print(element)


def move_up():
    """changes to parent directory"""
    os.chdir("..")


def move_down(cur_dir):
    """prompts for subdirectory name, validates, and changes to it"""
    my_dir = input("\nEnter directory name: ").strip()
    full_path = cur_dir + os.sep + my_dir

    if os.path.exists(full_path) and os.path.isdir(full_path):
        os.chdir(my_dir)
    else:
        print("Directory does not exist!")


def num_files(path):
    """recursively counts all files in path and subdirectories"""
    count = 0

    for element in os.listdir(path):
        full_path = path + os.sep + element

        if os.path.isfile(full_path):
            count += 1
        elif os.path.isdir(full_path):
            count += num_files(full_path)

    return count


def num_bytes(path):
    """recursively sums file sizes in path and subdirectories"""
    total = 0

    for element in os.listdir(path):
        full_path = path + os.sep + element

        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += num_bytes(full_path)

    return total


def find_files(my_file, path):
    """recursively searches for files matching substring, returns list of paths"""
    files = []

    for element in os.listdir(path):
        full_path = path + os.sep + element

        if os.path.isfile(full_path):
            if my_file in element:
                files.append(full_path)
        elif os.path.isdir(full_path):
            files.extend(find_files(my_file, full_path))

    return files
