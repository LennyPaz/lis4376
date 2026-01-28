#!/usr/bin/env python3
# functions.py
# Functions for SS1 - Python Lists
# Developer: Lenny Paz


def print_list(lst, description=""):
    """Print a list with optional description."""
    if description:
        print(f"{description}")
    print(lst)
    print()


def append_to_list(lst, element):
    """Append an element to the end of a list."""
    lst.append(element)
    return lst


def insert_at_beginning(lst, element):
    """Insert an element at the beginning of a list."""
    lst.insert(0, element)
    return lst


def get_list_length(lst):
    """Return the number of elements in a list."""
    return len(lst)


def reverse_list(lst):
    """Reverse the list in place."""
    lst.reverse()
    return lst


def remove_last_element(lst):
    """Remove and return the last element of a list."""
    return lst.pop()


def delete_by_index(lst, index):
    """Delete an element from list by index."""
    del lst[index]
    return lst


def delete_by_value(lst, value):
    """Delete an element from list by value."""
    lst.remove(value)
    return lst


def clear_list(lst):
    """Delete all elements from a list."""
    lst.clear()
    return lst


def sort_list(lst, reverse=False):
    """Sort the list alphabetically or reverse alphabetically."""
    lst.sort(reverse=reverse)
    return lst
