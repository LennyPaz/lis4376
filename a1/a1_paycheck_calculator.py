# Pay Check Calculator
# Program calculates net pay based upon hours worked, hourly rate, and taxes paid.

# Program Requirements:
# Developer: Lenny Paz
# 1. Must use float data type for user input.
# 2. Must round calculations to two decimal places.
# 3. Must format currency with dollar sign, and two decimal places.

print("Pay Check Calculator")
print("Program calculates net pay based upon hours worked, hourly rate, and taxes paid.")
print()
print("Program Requirements:")
print("Developer: Lenny Paz")
print("1. Must use float data type for user input.")
print("2. Must round calculations to two decimal places.")
print("3. Must format currency with dollar sign, and two decimal places.")
print()

# input:
print("User Input:")
hours = float(input("Hours Worked: "))
hourly_rate = float(input("Hourly Rate: $"))
tax_rate = float(input("Tax Rate (percent): "))
print()

# process:
gross_pay = hours * hourly_rate
tax_amount = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_amount

# output:
print("Program Output:")
print("Gross Pay:\t", "${:,.2f}".format(gross_pay))
print("Tax Rate:\t", "{:,.2%}".format(tax_rate/100))
print("Tax Amount:\t", "${:,.2f}".format(tax_amount))
print("Net Pay:\t", "${:,.2f}".format(net_pay))