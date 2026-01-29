#!/usr/bin/env python3
# main.py
# SS2 - Python Tuples
# Developer: Lenny Paz

from functions import (
    print_tuple, get_tuple_length, get_element_by_index,
    get_tuple_slice, count_element, create_tuple, delete_tuple_message
)

print("Python Tuples")
print()
print("Program Requirements:")
print("Developer: Lenny Paz")
print()
print("1. Tuples (Python data structure): \"Immutable\" (cannot be changed), ordered sequence of elements.")
print("2. Tuples are immutable/unchangeable--that is, cannot insert, update, delete.")
print("3. Note: Can reassign or delete an \"entire\" tuple, \"not\" individual items or slices.")
print("4. Tuple uses parentheses \"()\"--unlike lists \"[]\"--and one and two parentheses (), aka tuple \"packing\".")
print("5. Backward-engineer the following program.")
print()

# Create my_tuple
my_tuple = (1, 'c', 3, 'd', 5.5)

print("Print my_tuple:")
print(my_tuple)
print()

# Print my_tuple unpacking
a, b, c, d, e = my_tuple
print("Print my_tuple unpacking:")
print(f"steed1, c, steed1+steed2, d, steed+float")
print(a, b, c, d, e)
print()

# Display number of my_tuple elements
print("Display number of my_tuple elements:")
print(get_tuple_length(my_tuple))
print()

# Print element by index (access 3rd element)
print("Print element by index: my_tuple[2] (access 3rd element):")
print(get_element_by_index(my_tuple, 2))
print()

# Print "slice" of my_tuple
print("Print \"slice\" of my_tuple (access 2nd thru 4th elements):")
print(get_tuple_slice(my_tuple, 1, 4))
print()

# Reassign my_tuple using count() method
print("Reassign my_tuple using .count() method (no parentheses):")
count_val = count_element(my_tuple, 'c')
print(f"Count of 'c' in my_tuple: {count_val}")
print()

# Reassign my_tuple (delete and create anew)
print("Reassign my_tuple (delete and create anew):")
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)
print()

# Delete my_tuple
print("Delete my_tuple:")
del my_tuple
delete_tuple_message()
print()

# Verify tuple is deleted (will generate error if accessed)
print("Note: my_tuple will generate error if trying to print after delete, as it no longer exists.")
