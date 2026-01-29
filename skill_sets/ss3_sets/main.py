#!/usr/bin/env python3
# main.py
# SS3 - Python Sets (like mathematical sets)
# Developer: Lenny Paz

from functions import (
    create_empty_set, create_set_from_list, create_set_from_tuple,
    print_set, add_element, get_set_length, get_min_value,
    get_max_value, get_sum_values, discard_element, clear_set
)

print("Python Sets - like mathematical sets!")
print()
print("Program Requirements:")
print("Developer: Lenny Paz")
print()
print("1. Sets (Python data structure): mutable, heterogeneous, unordered sequence of elements, CANNOT contain duplicate values.")
print("2. Note: \"True\" and integer 1 are considered duplicates in sets, as are \"False\" and integer 0.")
print("3. Since sets mutable/changeable, they \"cannot\" contain other mutable items like list, set, or dictionary.")
print("4. Note: Since sets cannot contain duplicates, duplicates entered will only store first copy.")
print("5. Two methods to create sets:")
print("   a. Create a set using \"set()\" function: set1 = set()")
print("   b. Create a set using curly braces \"{}\": set1 = {\"value1\", \"value2\"}, can also convert a list or tuple to set.")
print("6. Backward-engineer the following program.")
print()

# Create set using set() function
set1 = create_empty_set()
print("Print set1 created using set() function: set1 = set():")
print(set1)
print()

# Create set with curly braces containing values
set2 = {'Ned', 'Robert', 2, 3.14, True}
print("Print set2 created using curly braces {} (i.e., curly brackets), \"regardless\" of how they were created:")
print("Note: \"Value added\" using 'add()' in subsequent code below...")
print(set2)
print()

# Print set3 created using set() function with list
set3 = create_set_from_list([True, 1, 3.14, 3, 'test'])
print("Print set3 created using set() function with list:")
print(set3)
print()

# Print set4 created using set() function with tuple
set4 = create_set_from_tuple((True, 1, 3.14, 3, 'test'))
print("Print set4 created using set() function with tuple:")
print(set4)
print()

# Add an element using add() method
print("Add an element (5) using add() method:")
add_element(set2, 5)
print(set2)
print()

# Display updated set2 elements
print("Display updated set2 elements:")
print(set2)
print()

# Create numeric set for min, max, sum operations
set5 = {True, 1, 3.14, 3, 5}
print("Display set5 with following values: 1, 3.14, 3, True (Note: True==1, and value 3 already exist):")
print(set5)
print()

# Length of set5
print("Length of set5:")
print(get_set_length(set5))
print()

# Remove element from set
set6 = {True, 3.14, 3, 5}
discard_element(set6, True)
print("Removed:")
print(set6)
print()

# Length after removal
print("Length of set6:")
print(get_set_length(set6))
print()

# Note about deleting set element that doesn't exist
print("Note: When deleting set element that doesn't exist, discard() ignores it, but remove() raises KeyError!")
print()

# Display minimum value
set7 = {3.14, 3, 5, 1}
print("Display minimum value: \"min()\":")
print(get_min_value(set7))
print()

# Display maximum value
print("Display maximum value: \"max()\":")
print(get_max_value(set7))
print()

# Display sum of values (must be numeric)
print("Display sum of values (\"must\" be numeric, to able to convert to numeric):")
print(get_sum_values(set7))
print()

# Clear set elements
print("Clear set elements:")
clear_set(set7)
print(set7)
print()

# Length of empty set
print("Length of set7:")
print(get_set_length(set7))
