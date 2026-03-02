#!/usr/bin/env python3
"""SS7 - Pseudo-Random Number Lists"""
import functions as f


def main():
    """main function for pseudo-random number list operations"""
    # initialize variable(s)
    size = 0
    your_list = []  # create empty list

    # function calls
    f.get_requirements()
    size = f.get_list_size()
    your_list = f.create_list(size)
    print(your_list)  # check pseudo-random number list
    f.sort_list(your_list)


if __name__ == "__main__":
    main()
