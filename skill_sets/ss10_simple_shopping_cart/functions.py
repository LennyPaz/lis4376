#!/usr/bin/env python3
"""SS10 - Functions for Simple Shopping Cart

Defines five functions:

1. get_requirements()
2. add_items()
3. get_items_cost()
4. get_tax_rate()
5. get_cart()
"""


def get_requirements():
    """prints developer info and program requirements"""
    print("\nDeveloper: Lenny Paz")
    print("Simple Shopping Cart!")
    print("\nProgram Requirements:\n"
          + "1. Capture user-entered shopping items.\n"
          + "2. Retrieve cost for each item.\n"
          + "3. Print items, cost, and total of all items.\n"
          + "4. Must perform data and range validation.\n")

    print("***Extra credit (10 pts):***\n"
          + "a. Request tax rate: between 1% and 10%.\n"
          + "b. Print pre-tax total, total tax, and total amount with tax.\n"
          + "c. Must perform data and range validation.\n")

    print("***Resource(s):***\n"
          + "Prompt user until valid response: https://www.python-engineer.com/posts/ask-user-for-input/\n"
          + "Print tabular data:\n"
          + "  https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data\n"
          + "  https://www.educba.com/python-print-table/\n")

    print("Input:\n"
          + "Enter -1 to stop program.\n")


def add_items():
    """prompts for item names with validation, returns list of items"""
    your_items = []
    counter = 1

    while True:
        try:
            item = input("Enter item" + str(counter) + " name: ")

            if item.strip()[0:1] == "":
                raise IndexError

            if item.strip() == "-1":
                print("Stopping list!")
                break

            your_items.append(item.strip())
            counter += 1

        except IndexError:
            print("No item name entered! Try again.\n")

    return your_items


def get_items_cost(items_list):
    """prompts for cost of each item with data and range validation, returns list of costs"""
    your_costs = []

    for i in range(len(items_list)):
        while True:
            try:
                cost = float(input("Enter " + items_list[i] + " cost: $"))

                if cost < 1 or cost > 100:
                    print("Item cost must be between $1 and $100.\n")
                    continue

                your_costs.append(cost)
                break

            except ValueError:
                print("Not a float! Try again.\n")

    return your_costs


def get_tax_rate():
    """prompts for tax rate with data and range validation, returns float"""
    while True:
        try:
            tax = float(input("Enter tax rate (1% - 10%): "))

            if tax < 1 or tax > 10:
                print("Tax rate must be between 1% and 10%.\n")
                continue

            return tax

        except ValueError:
            print("Not a float! Try again.\n")


def get_cart(items, costs, tax):
    """prints formatted shopping cart with pre-tax total, tax, and total with tax"""
    print("\n{0:<10s} {1:>6s}".format("Item", "Cost"))

    for j in range(len(items)):
        print("{0:<10s} {1:>6.2f}".format(items[j], costs[j]))

    pre_tax = sum(costs)
    tax_amount = pre_tax * tax
    total = pre_tax + tax_amount

    print("\nTotal: ${0:.2f}".format(pre_tax))
    print("Total Tax {0:.2f}%: ${1:.2f}".format(tax * 100, tax_amount))
    print("Total Amount with Tax: ${0:,.2f}".format(total))
