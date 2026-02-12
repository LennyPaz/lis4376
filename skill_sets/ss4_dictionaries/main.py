#!/usr/bin/env python3
"""SS4 - Python Dictionaries"""
import functions as f


def main():
    """main function for dictionary operations"""
    f.get_requirements()
    your_dictionary = f.get_dictionary()
    f.parse_dictionary(your_dictionary)
    f.count_dictionary(your_dictionary)
    f.add_element(your_dictionary)
    f.update_element(your_dictionary)
    f.delete_element(your_dictionary)
    f.delete_dictionary(your_dictionary)


if __name__ == "__main__":
    main()
