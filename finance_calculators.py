import math

# Use if-elif-else statments to determine the type of calculation:
# "if" input is "investment", perform investment calculation;
# "else if" input is "bond", perform bond calculation;
# "else" the input is incorrect, display error message.

calc_type = input("""Investment - to calculate the amount of interest you'll earn on your investment.
Bond - to calculate the amount you"ll have to pay on a home loan.
    
Enter either "investment" or "bond" from the menu above to proceed: """
)

print("")

# Calculate the investment interest by requesting the required input values.
# Inputs stored as float variables.
if calc_type.casefold() == "investment".casefold():

    deposit = float(input("Please enter the amount of money that will be deposited: R "))
    interest_invest = float(input("Please enter the interest rate amount as a percentage value (i.e. if 7%, enter: 7): "))
    years_invest = float(input("Please enter the planned amount of years for the investment: "))
    interest = input("Please enter the type of interest for the calculation, by typing either \"simple\" or \"compound\": ")
    
    # Again, use if-elif-else statments to calculate based on interest type inputted.
    if interest.casefold() == "simple".casefold():

        total_simple = round((deposit * (1 + (interest_invest / 100) * years_invest)), 2)     # Round to 2 decimal places.

        # Display the total amount earned with simple interest.
        print(f"\nThe amount given back after {years_invest} years at an interest rate of {interest_invest} %, "
              f"calculated with {interest.casefold()} interest, is: R {total_simple}.")

    elif interest.casefold() == "compound".casefold():

        total_compound = round((deposit * math.pow((1 + (interest_invest / 100)),years_invest)), 2)

        # Display the total amount earned with compound interest.
        print(f"\nThe amount given back after {years_invest} years at an interest rate of {interest_invest} %, "
              f"calculated with {interest.casefold()} interest, is: R {total_compound}.")

    # If "simple" or "compound" were typed incorrectly, display an error message.
    else:
        print("\nYou have incorrectly entered an option. Please run the program again.")

elif calc_type.casefold() == "bond".casefold():

    house_value = float(input("Please enter the present value of the house: R "))
    interest_bond = float(input("Please enter the annual interest rate amount as a percentage value (i.e. if 7%, enter: 7): "))
    months_bond = float(input("Please enter the planned amount of months to repay the bond: "))

    repayment = round(((interest_bond / 12 / 100) * house_value) / (1 - (1 + (interest_bond / 12 / 100))**(-(months_bond))),2)

    # Display the monthly repayment amount.

    print(f"\nThe monthly repayment on a bond amount of R {house_value} over {months_bond} months "
          f"at an interest rate of {interest_bond} % will be: R {repayment}.")

# Display an error message if the first input was typed incorrectly.
else:
    print("You have incorrectly entered an option. Please run the program again.")
