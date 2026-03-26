# Pseudocode - By Roe Wiid - Task = finance_calculators.py
#
# Type input function to get user to choose which calculation
# they want to do.

# The first output that the user sees when the program runs
# should look like this:
# Investment - to calculate the amount of interest you'll earn
# on your investment.
# Bond - to calculate the amount you'll have to pay on a home
# loan.
# Enter either "investment" or "bond" from the menu above to
# proceed:

# The user should be able to enter their choice in either upper case or
# lower case.

# If the user selects "investment" the program should calculate the amount
# of interest that will be earned on the investment.

# Once interest is selected the program should ask the user to input the
# following:
# The amount of money that the user is depositing (the principal)
# The interest rate (as a percentage)
# The number of years they plan on investing the money for

# Provide an option ask the user to choose between simple interest and
# compound interest.

# The formula for simple interest is:  A = P(1 + rt)
# The formula for compound interest is:  A = P(1 + r)^t

# If the user selects "bond" the program should calculate the
# amount that the user will have to pay on a home loan.

# Once type of interest is selected the program should ask the
# user to input the following:
# The present value of the house (the principal)
# The interest rate (as a percentage)
# The number of months they plan to take to repay the bond

# The formula to calculate the monthly repayment is:
# x = (i.P) / (1 - (1 + i)^(-n))

# Output the result of the calculation to the user.

# Get user input for the type of calculation

print()
print("These are the available calculations which you can choose:")

print()
print("\033[31m (1) Investment - to calculate the amount of "
      "interest you'll earn on your investment.\033[0m")

print()
print("\033[94m (2) Bond - to calculate the amount you'll have "
      "to pay on a home loan.\033[0m")

print()
type_of_calculation = input(
    "Please choose a calculation type (investment or bond): "
).lower()

if type_of_calculation == "investment":
    # Get user input for investment details
    principal = float(input(
        "\033[31mEnter the amount of money you are depositing: "
    ))
    interest_rate = float(input(
        "\033[31mEnter the interest rate (as a percentage): "
    )) / 100
    years = int(input(
        "\033[31mEnter the number of years you plan on investing: "
    ))
    interest_type = input(
        "\033[31mChoose the type of interest "
        "(simple or compound): "
    ).lower()

    if interest_type == "simple":
        # Calculate simple interest
        amount = principal * (1 + interest_rate * years)
        print(f"\033[31mThe total amount after {years} years will be: "
              f"{amount:.2f}\033[0m")
    elif interest_type == "compound":
        # Calculate compound interest
        amount = principal * (1 + interest_rate) ** years
        print(f"\033[31mThe total amount after {years} years will be: "
              f"{amount:.2f}\033[0m")
    else:
        print("Invalid interest type. Please choose either "
              "'simple' or 'compound'.")
elif type_of_calculation == "bond":
    # Get user input for bond details
    present_value = float(input(
        "\033[94mEnter the present value of the house: \033[0m"
    ))
    interest_rate = float(input(
        "\033[94mEnter the interest rate (as a percentage): \033[0m"
    )) / 100 / 12
    months = int(input(
        "\033[94mEnter the number of months you plan to take to "
        "repay the bond: \033[0m"
    ))

    # Calculate monthly repayment
    monthly_repayment = (interest_rate * present_value) / (
        1 - (1 + interest_rate) ** (-months)
    )
    print(f"\033[94mThe monthly repayment will be: "
          f"{monthly_repayment:.2f}\033[0m")
else:
    print("Invalid calculation type. Please choose either "
          "'investment' or 'bond'.")
