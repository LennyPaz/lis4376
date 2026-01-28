#!/usr/bin/env python3
# functions.py
# Functions for SS2 - Python Tuples
# Developer: Lenny Paz


def print_tuple(tpl, description=""):
    """Print a tuple with optional description."""
    if description:
        print(f"{description}")
    print(tpl)
    print()


def unpack_tuple(tpl):
    """Unpack and return tuple elements."""
    return tpl


def get_tuple_length(tpl):
    """Return the number of elements in a tuple."""
    return len(tpl)


def get_element_by_index(tpl, index):
    """Get an element from tuple by index."""
    return tpl[index]


def get_tuple_slice(tpl, start, end):
    """Get a slice of the tuple."""
    return tpl[start:end]


def count_element(tpl, element):
    """Count occurrences of an element in tuple."""
    return tpl.count(element)


def find_index(tpl, element):
    """Find the index of an element in tuple."""
    return tpl.index(element)


def create_tuple(*args):
    """Create a new tuple from arguments."""
    return tuple(args)


def delete_tuple_message():
    """Display message about deleting tuple."""
    print("Tuple deleted using 'del' method.")
