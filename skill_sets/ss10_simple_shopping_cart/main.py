#!/usr/bin/env python3
"""SS10 - Simple Shopping Cart with Data Validation"""
import functions as f


def main():
    """main function for simple shopping cart"""
    # initialize variable(s)
    your_items = []
    your_costs = []
    tax_rate = 0.0

    # function calls
    f.get_requirements()
    your_items = f.add_items()

    if len(your_items) == 0:
        print("No shopping cart items.")
    else:
        your_costs = f.get_items_cost(your_items)
        tax_rate = f.get_tax_rate() / 100.0
        f.get_cart(your_items, your_costs, tax_rate)


if __name__ == "__main__":
    main()
