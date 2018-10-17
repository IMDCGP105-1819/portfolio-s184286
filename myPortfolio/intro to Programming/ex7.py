
"""
Task 3

You’ve graduated and need to move to London to start your new job,
you’ve decided that you want to start saving to buy a house.
You’re going to have to save for several years to be able to afford a deposit.
Write a program that will help you calculate how long it will take you to save up for a deposit. savings value

1. The cost of the house is total_cost
2. The portion of the total cost needed for a deposit is portion_deposit, to make that easier, assume it to be 20% (0.20).
3. Call the amount you have saved so far current_savings, you start with £0.
4. Assume that you invest wisely, with an annual return of r (in other words, at the end of each month you receive an additional current_savings*r/12. Assume that our investments earn a return of r = 0.04 (4%).
5. Assume your annual salary is annual_salary.
6. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that portion_saved, this variable should be in decimal form (i.e. 0.1 for 10%).
7. At the end of each month, your savings will be increased by the return of your investment, plus a percentage of your monthly_salary (annual_salary / 12).

Your program should ask the user to enter the following variables:

    • The starting annual salary (annual_salary)
    • The portion of salary to be saved (portion_saved)
    • The cost of your dream home (total_cost)

You will want your main variables to be floats, so you should cast user inputs to floats.

To help get you started, here is a rough outline of the stages you should probably follow:

    • Retrieve user input. For this task, you can assume the users will enter valid input (they won’t enter a string when you request an int).
    • Initialize some state variables. You should decide what information you need – be careful about values that represent annual amounts and those that represent monthly amounts.

Try different inputs and see how long it takes to save for a down payment.

Your program must print results in the following format:

Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183

Save your work as ex7.py and commit regularly to GitHub.


"""

#inputs

annual_salary=float(input("Enter your annual salary:"))                                     # income - yr value
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))      # *10% monthly savings
total_cost=float(input("Enter the cost of your dream home:"))                               # property value

# values
monthly_salary=annual_salary/12                                                             # income - monthly value

portion_deposit= total_cost * 0.20                                                                        # 20% depoist value
current_savings=0                                                                            #current savings value
r= (current_savings * 0.4)/12
months_required=0                                                                            # number of months required to save for a depoist.


#sum
while(current_savings< total_cost * portion_deposit):
    current_savings+=monthy_salary*portion_saved
    current_savings+=current_savings*r/12
    months_required+=1
print(f"Total number of months required to save for a depoist: {months_required}")             # final output.
