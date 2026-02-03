#!/usr/bin/env python3
"""SS3 - Functions for Python Sets"""


def get_requirements():
    """prints the program requirements"""
    print("Python Sets - like mathematical sets!")
    print()
    print("Program Requirements:")
    print("Developer: Lenny Paz")
    print()
    print("1. Sets (Python data structure): mutable, heterogeneous, unordered sequence of elements, CANNOT contain duplicate values.")
    print('2. Note: "True" and integer 1 are considered duplicates in sets, as are "False" and integer 0.')
    print('3. Since sets mutable/changeable, they "cannot" contain other mutable items like list, set, or dictionary.')
    print("4. Note: Since sets cannot contain duplicates, duplicates entered will only store first copy.")
    print("5. Two methods to create sets:")
    print('   a. Create a set using "set()" function: set1 = set()')
    print('   b. Create a set using curly braces "{}": set1 = {"value1", "value2"}, can also convert a list or tuple to set.')
    print("6. Backward-engineer the following program.")
    print()


def create_sets():
    """creates sets in different ways and prints them, returns set2"""
    # create empty set using set()
    set1 = set()
    print("Print set1 created using set() function: set1 = set():")
    print(set1)
    print()

    # create set using curly braces
    set2 = {'Ned', 'Robert', 2, 3.14, True}
    print('Print set2 created using curly braces {} (i.e., curly brackets), "regardless" of how they were created:')
    print("Note: \"Value added\" using 'add()' in subsequent code below...")
    print(set2)
    print()

    # create set from a list
    set3 = set([True, 1, 3.14, 3, 'test'])
    print("Print set3 created using set() function with list:")
    print(set3)
    print()

    # create set from a tuple
    set4 = set((True, 1, 3.14, 3, 'test'))
    print("Print set4 created using set() function with tuple:")
    print(set4)
    print()

    return set2


def add_to_set(set2):
    """adds an element to set2 and prints it"""
    print("Add an element (5) using add() method:")
    set2.add(5)
    print(set2)
    print()

    print("Display updated set2 elements:")
    print(set2)
    print()


def set_length_demo():
    """demonstrates set length and discard with set5 and set6"""
    # set5 with duplicates (True==1)
    set5 = {True, 1, 3.14, 3, 5}
    print("Display set5 with following values: 1, 3.14, 3, True (Note: True==1, and value 3 already exist):")
    print(set5)
    print()

    print("Length of set5:")
    print(len(set5))
    print()

    # discard True from set6
    set6 = {True, 3.14, 3, 5}
    set6.discard(True)
    print("Removed:")
    print(set6)
    print()

    print("Length of set6:")
    print(len(set6))
    print()

    print("Note: When deleting set element that doesn't exist, discard() ignores it, but remove() raises KeyError!")
    print()


def set_stats():
    """displays min, max, sum and clears set7"""
    set7 = {3.14, 3, 5, 1}

    print('Display minimum value: "min()":')
    print(min(set7))
    print()

    print('Display maximum value: "max()":')
    print(max(set7))
    print()

    print('Display sum of values ("must" be numeric, to able to convert to numeric):')
    print(sum(set7))
    print()

    # clear set7
    print("Clear set elements:")
    set7.clear()
    print(set7)
    print()

    print("Length of set7:")
    print(len(set7))
