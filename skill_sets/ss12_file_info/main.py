#!/usr/bin/env python3
"""SS12 - File Info"""
import functions as f


def main():
    """main function for file info navigator"""
    # function calls
    f.get_requirements()

    while True:
        f.get_menu()
        command = f.get_command()

        if command != "7":
            f.run_command(command)
        else:
            print("\nStopping program!\n")
            break


if __name__ == "__main__":
    main()
