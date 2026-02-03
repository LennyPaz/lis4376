#!/usr/bin/env python3
"""SS2 - Functions for Python Tuples"""


def get_requirements():
    """prints the program requirements"""
    print("Python Tuples")
    print()
    print("Program Requirements:")
    print("Developer: Lenny Paz")
    print()
    print('1. Tuples (Python data structure): "Immutable" (cannot be changed), ordered sequence of elements.')
    print("2. Tuples are immutable/unchangeable--that is, cannot insert, update, delete.")
    print('3. Note: Can reassign or delete an "entire" tuple, "not" individual items or slices.')
    print('4. Tuple uses parentheses "()"--unlike lists "[]"--and one and two parentheses (), aka tuple "packing".')
    print("5. Backward-engineer the following program.")
    print()


def get_tuple():
    """creates and returns my_tuple"""
    my_tuple = (1, 'c', 3, 'd', 5.5)
    return my_tuple


def unpack_tuple(my_tuple):
    """unpacks the tuple and prints each element"""
    print("Print my_tuple:")
    print(my_tuple)
    print()

    a, b, c, d, e = my_tuple
    print("Print my_tuple unpacking:")
    print(f"steed1, c, steed1+steed2, d, steed+float")
    print(a, b, c, d, e)
    print()


def count_tuple(my_tuple):
    """counts occurrences of 'c' in the tuple"""
    print("Reassign my_tuple using .count() method (no parentheses):")
    count_val = my_tuple.count('c')
    print(f"Count of 'c' in my_tuple: {count_val}")
    print()


def parse_tuple(my_tuple):
    """displays length, index access, and slicing"""
    print("Display number of my_tuple elements:")
    print(len(my_tuple))
    print()

    # access 3rd element by index
    print("Print element by index: my_tuple[2] (access 3rd element):")
    print(my_tuple[2])
    print()

    # slice 2nd thru 4th elements
    print('Print "slice" of my_tuple (access 2nd thru 4th elements):')
    print(my_tuple[1:4])
    print()


def reassign_tuple(my_tuple):
    """reassigns the tuple to new values"""
    print("Reassign my_tuple (delete and create anew):")
    my_tuple = (10, 20, 30, 40, 50)
    print(my_tuple)
    print()


def remove_tuple(my_tuple):
    """deletes the tuple using del"""
    print("Delete my_tuple:")
    del my_tuple
    print("Tuple deleted using 'del' method.")
    print()
    print("Note: my_tuple will generate error if trying to print after delete, as it no longer exists.")
