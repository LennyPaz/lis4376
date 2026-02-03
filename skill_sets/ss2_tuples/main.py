#!/usr/bin/env python3
"""SS2 - Python Tuples"""
import functions as f


def main():
    """main function for tuple operations"""
    f.get_requirements()
    my_tuple = f.get_tuple()
    f.unpack_tuple(my_tuple)
    f.parse_tuple(my_tuple)
    f.count_tuple(my_tuple)
    f.reassign_tuple(my_tuple)
    f.remove_tuple(my_tuple)


if __name__ == "__main__":
    main()
