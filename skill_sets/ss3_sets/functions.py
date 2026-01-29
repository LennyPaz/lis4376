#!/usr/bin/env python3
# functions.py
# Functions for SS3 - Python Sets
# Developer: Lenny Paz


def create_empty_set():
    """Create an empty set using set() function."""
    return set()


def create_set_from_list(lst):
    """Create a set from a list."""
    return set(lst)


def create_set_from_tuple(tpl):
    """Create a set from a tuple."""
    return set(tpl)


def print_set(s, description=""):
    """Print a set with optional description."""
    if description:
        print(f"{description}")
    print(s)
    print()


def add_element(s, element):
    """Add an element to the set."""
    s.add(element)
    return s


def get_set_length(s):
    """Return the number of elements in a set."""
    return len(s)


def get_min_value(s):
    """Return the minimum value in the set."""
    return min(s)


def get_max_value(s):
    """Return the maximum value in the set."""
    return max(s)


def get_sum_values(s):
    """Return the sum of numeric values in the set."""
    return sum(s)


def remove_element(s, element):
    """Remove an element from the set."""
    s.remove(element)
    return s


def discard_element(s, element):
    """Discard an element from the set (no error if not found)."""
    s.discard(element)
    return s


def clear_set(s):
    """Clear all elements from the set."""
    s.clear()
    return s
