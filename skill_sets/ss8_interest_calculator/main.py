#!/usr/bin/env python3
"""SS8 - Interest Calculator"""
import functions as f


def main():
    """main function for compound interest calculator"""
    # function calls
    f.get_requirements()

    command = ""
    while command != "e":
        f.display_menu()
        command = f.get_command()
        if command == "e":
            break

        # initialize variable(s)
        principal = 0.0
        rate = 0.0
        years = 0

        principal = f.get_principal()
        rate = f.get_rate()
        years = f.get_years()
        f.calculate_interest(principal, rate, years, command)

    print("\nThank you for using our compound interest program!\n")


if __name__ == "__main__":
    main()
