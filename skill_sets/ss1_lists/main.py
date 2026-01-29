#!/usr/bin/env python3
# main.py
# SS1 - Python Lists
# Developer: Lenny Paz

from functions import (
    print_list, append_to_list, insert_at_beginning, get_list_length,
    reverse_list, remove_last_element, delete_by_index, delete_by_value,
    clear_list, sort_list
)

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

# Create list1
list1 = [1, 'test', 3.14, True]

print("Print list:")
print(list1)
print()

# Append character to end of list
append_to_list(list1, '@')
print("Print character to end of list:")
print(list1)
print()

# Insert element at beginning of list
insert_at_beginning(list1, 6)
print("Insert element at beginning of list:")
print(list1)
print()

# Display number of list elements
print("Display number of list elements:")
print(get_list_length(list1))
print()

# Reverse list
reverse_list(list1)
print("Reverse list:")
print(list1)
print()

# Remove last list element
removed = remove_last_element(list1)
print("Remove last list element:")
print(list1)
print()

# Create list2
list2 = ['@', 'test', 3.14, 'test', 1]

# Delete second element from list2 by index (note: index 1=2nd element)
delete_by_index(list2, 1)
print("Delete second element from list2 by \"index\" (note: index 1=2nd element):")
print(list2)
print()

# Delete element from list1 by value (3.14)
delete_by_value(list1, 3.14)
print("Delete element from list1 by \"value\" (3.14):")
print(list1)
print()

# Delete all elements from list1
clear_list(list1)
print("Delete all elements from list1:")
print(list1)
print()

# Create list2 for sorting demonstration
list2 = ['true', 'w', 'more', 'love']
print("Print list2:")
print(list2)
print()

# Sort elements in list2 alphabetically
sort_list(list2)
print("Sort elements in list2 alphabetically - using sort():")
print(list2)
print()

# Sort elements in list2 reverse alphabetically
sort_list(list2, reverse=True)
print("Sort elements in list2 reverse alphabetically - using sort():")
print(list2)
