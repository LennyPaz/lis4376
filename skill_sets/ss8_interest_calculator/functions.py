"""SS8 - Functions for Interest Calculator

Defines seven functions:

1. get_requirements()
2. display_menu()
3. get_command()
4. get_principal()
5. get_rate()
6. get_years()
7. calculate_interest()

Compound Interest Formula: A = P(1 + r/n)^(nt)
P = Principal amount (the beginning balance).
r = Interest rate (per year, expressed as a decimal).
n = Number of times interest is compounded per year.
t = Number of years.
"""


def get_requirements():
    """prints the program requirements"""
    print("\nDeveloper: Lenny Paz")
    print("Compound Interest Investment Report Program")
    print("\nProgram Requirements:\n"
          + "1. Write a program that prints a compound interest report table.\n"
          + "2. Must perform data validation.\n"
          + "3. ***Extra credit!***\n"
          + "\tInstead of annual compound interest rate formula, calculate interest based on\n"
          + "\tuser-entered compound interest rate: yearly, quarterly, monthly, or daily.\n"
          + "4. Backward-engineer program output below.\n")

    print("***Resource(s):***\n"
          + "https://www.fool.com/saving/how-often-is-interest-accrued-on-a-savings-account.aspx\n"
          + "https://www.nerdwallet.com/article/banking/how-to-calculate-interest-in-a-savings-account\n"
          + "Verify calculation: https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator\n")

    print("Input:")


def display_menu():
    """displays the compounding frequency menu"""
    print("\nMENU:")
    print("y=Yearly")
    print("q=Quarterly")
    print("m=Monthly")
    print("d=Daily")
    print("e=Exit")


def get_command():
    """prompts for menu command with validation, returns command string"""
    valid_commands = ["y", "q", "m", "d", "e"]
    while True:
        command = input("\nEnter command: ").lower().strip()
        if command in valid_commands:
            return command
        else:
            print("Invalid command! Please enter y, q, m, d, or e.")


def get_principal():
    """prompts for principal amount with data validation, returns float"""
    # test valid float and w/in range
    while True:
        try:
            # initialize variable(s)
            principal = 0.0

            # prompt initial investment amount
            principal = float(input("Enter principal: $"))

            is_within_range = False
            while not is_within_range:
                if principal >= 1 and principal <= 1000000:
                    is_within_range = True
                else:
                    print("Principal must be between $1 and $1,000,000.\n")
                    principal = float(input("Enter principal: $"))

        except ValueError:
            print("Not a float! Try again.\n")
            continue
        else:
            return principal


def get_rate():
    """prompts for interest rate with data validation, returns float"""
    # test valid float and w/in range
    while True:
        try:
            # initialize variable(s)
            rate = 0

            # prompt interest rate
            rate = float(input("Enter rate (%): "))

            is_within_range = False
            while not is_within_range:
                if rate >= 1 and rate <= 10:
                    is_within_range = True
                else:
                    print("Rate must be between 1% and 10% (no percent sign!).\n")
                    rate = float(input("Enter rate (%): "))

        except ValueError:
            print("Not a float! Try again.\n")
            continue
        else:
            return rate


def get_years():
    """prompts for number of years with data validation, returns int"""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            years = 0

            # prompt investment years
            years = int(input("Enter years: "))

            is_within_range = False
            while not is_within_range:
                if years >= 1 and years <= 50:
                    is_within_range = True
                else:
                    print("Years must be between 1 and 50.\n")
                    years = int(input("Enter years: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return years


def calculate_interest(principal, rate, years, command):
    """calculates and displays compound interest table based on compounding frequency"""
    total_interest = 0.0  # initialize accumulator for interest
    rate = rate / 100  # convert rate to decimal value

    # map command to compounding period
    periods = {"y": 1, "q": 4, "m": 12, "d": 365}
    period = periods[command]

    # display table header
    print("\n{0:<4s} {1:>12s} {2:>12s} {3:>12s}".format(
        "Year", "Starting", "Interest", "Ending"))

    # compute and display yearly results
    for year in range(1, years + 1):
        period_interest = 0.0  # reset period interest value
        period_principal = principal  # set period principal to accumulated principal

        for p in range(1, period + 1):
            interest = period_principal * (rate / period)  # calculate interest for rate divided by period
            period_principal += interest  # accumulate principal for compounding
            period_interest += interest  # save interest accumulated to display on table

        end_principal = principal + period_interest  # accumulate new principal after cycle

        print("{0:>4d} {1:>12,.2f} {2:>12,.2f} {3:>12,.2f}".format(
            year, principal, period_interest, end_principal))

        principal = end_principal
        total_interest += period_interest

    # display totals
    print("\nEnding principal: ${0:,.2f}".format(end_principal))
    print("Total interest earned: ${0:,.2f}".format(total_interest))
