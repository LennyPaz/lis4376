#!/usr/bin/env python3
"""SS3 - Python Sets"""
import functions as f


def main():
    """main function for set operations"""
    f.get_requirements()
    set2 = f.create_sets()
    f.add_to_set(set2)
    f.set_length_demo()
    f.set_stats()


if __name__ == "__main__":
    main()
