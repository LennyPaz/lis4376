#!/usr/bin/env python3
"""SS1 - Functions for Python Lists"""


def get_requirements():
    """prints the program requirements"""
    print("Python Lists")
    print()
    print("Program Requirements:")
    print("Developer: Lenny Paz")
    print()
    print("1. Lists (Python data structure): mutable, ordered sequence of elements.")
    print("2. Lists are mutable/changeable--that is, can insert, update, delete.")
    print("3. Create two lists - using square brackets [list items]: list = [include below list elements here...]")
    print("4. Backward-engineer the following program.")
    print()


def get_list():
    """creates and returns list1"""
    list1 = [1, 'test', 3.14, True]
    return list1


def add_elements(list1):
    """appends and inserts elements into list1"""
    # print original list
    print("Print list:")
    print(list1)
    print()

    # append '@' character to end of list
    list1.append('@')
    print("Print character to end of list:")
    print(list1)
    print()

    # insert 6 at beginning of list
    list1.insert(0, 6)
    print("Insert element at beginning of list:")
    print(list1)
    print()


def list_info(list1):
    """displays length and reverses the list"""
    print("Display number of list elements:")
    print(len(list1))
    print()

    list1.reverse()
    print("Reverse list:")
    print(list1)
    print()


def remove_elements(list1):
    """removes elements from list1 and list2 in different ways"""
    # pop last element
    list1.pop()
    print("Remove last list element:")
    print(list1)
    print()

    # create list2 for delete by index demo
    list2 = ['@', 'test', 3.14, 'test', 1]

    # delete second element from list2 by index
    del list2[1]
    print('Delete second element from list2 by "index" (note: index 1=2nd element):')
    print(list2)
    print()

    # delete element from list1 by value
    list1.remove(3.14)
    print('Delete element from list1 by "value" (3.14):')
    print(list1)
    print()


def clear_list(list1):
    """clears all elements from list1"""
    list1.clear()
    print("Delete all elements from list1:")
    print(list1)
    print()


def sort_list():
    """creates list2 and sorts it both ways"""
    list2 = ['true', 'w', 'more', 'love']
    print("Print list2:")
    print(list2)
    print()

    # sort alphabetically
    list2.sort()
    print("Sort elements in list2 alphabetically - using sort():")
    print(list2)
    print()

    # sort reverse alphabetically
    list2.sort(reverse=True)
    print("Sort elements in list2 reverse alphabetically - using sort():")
    print(list2)
