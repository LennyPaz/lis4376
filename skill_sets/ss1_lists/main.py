#!/usr/bin/env python3
"""SS1 - Python Lists"""
import functions as f


def main():
    """main function for list operations"""
    f.get_requirements()
    list1 = f.get_list()
    f.add_elements(list1)
    f.list_info(list1)
    f.remove_elements(list1)
    f.clear_list(list1)
    f.sort_list()


if __name__ == "__main__":
    main()
