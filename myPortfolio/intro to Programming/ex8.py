"""

Task 1

Last week, we somewhat unrealistically assumed that while saving for a house you would never earn
a raise. That seems harsh, so let’s go back and fix that by saying that we’ll get a raise every 6 months.

Open ex7.py and save a new copy as ex8.py. Modify the code in the following ways:

1. Have the user input a semi-annual salary raise: semi_annual_raise (as a decimal percentage)
2. After the 6th month, increase your salary by that percentage. Do the same every 6 months
after that (12th, 18th etc).

Your output should be identical to the last attempt except for the addition of the new user input.
Be sure to commit each attempt at this problem to the portfolio repository, not just your final piece
of code.

git .
git commit -m “useful commit message”
git push


"""
## House deposit save time calculator
DEPOSIT_RATE = 0.2
SAVINGS_INTEREST_RATE = 0.04

# Get required data from user
salary = float(input("Enter your annual salary:"))
total_cost = float(input("Enter the cost of your dream home:"))
saved_portion = float(input("Enter the percent of your salary to save, as a decimal:")) / 100

# Calculate required values
savings_target = total_cost * DEPOSIT_RATE
monthly_savings = salary * saved_portion / 12

# Track savings over time
current_savings = monthly_savings
total_time = 0

# Increment time until target savings reached
while(current_savings < savings_target):
    current_savings += (current_savings * SAVINGS_INTEREST_RATE) + monthly_savings
    total_time += 1

# Display results
print(f"Deposit: £{savings_target: .2f}")
print(f"Monthly Savings: £{monthly_savings: .2f}")
print(f"Time: {total_time} months")
