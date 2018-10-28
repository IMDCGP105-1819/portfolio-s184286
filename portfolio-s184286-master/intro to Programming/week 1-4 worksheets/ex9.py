"""

Task 2

Let’s re-work how we approach the saving goal; rather than saying how long it might take us to save
up a specific value, let’s ask how much we need to save to achieve a specific target goal in a given
time period.

To simply things a little, we can make the following assumptions:
1. Your semi-annual raise is 0.07 (7%).
2. Your investments have an annual rate of return of 0.04 (4%).
3. The down payment is 0.25 (25%) of the cost of the house.
4. The cost of the house you are saving for is £1M.

You are now going to attempt to find the best rate of savings to achieve a down payment to a
million-pound house in 36 months. Rather than trying to hit that value exactly, there is a £100 leeway
either side of the deposit value.
In ex9.py, write a program to calculate the best savings rate, as a function of your starting salary. You
should use a bisection search to do this efficiently. You should keep track of the number of steps
required for your search to finish. You should be able to reuse some existing code to help solve this
problem.

Because we are searching for a value that is in principle a float (the best rate of savings) we are going
to limit ourselves to two decimal places – we may want to save at 7.04%, but we are not going to
worry about the difference between 7.041% and 7.039%. This means we can search for an integer
between 0 and 10000 and then convert it to a decimal percentage to use when we are calculating 
the current_savings after 36 months. This range allows us to avoid a possible infinite loop that could
arise were we searching the infinite number of decimals between 0 and 1.
Your program should allow you to enter different values for the starting salary and it should account
for the fact that some salaries will not allow you to save the required amount within 3 years.

Hints
    • There may be multiple savings rates that yield a savings amount that is within £100 of the required deposit. In this case, you can just return any of the possible values.
    • Depending on your stopping condition and how you compute a trial value for bisection search, your number of steps may vary from the example below.
    • Watch out for integer division when calculating if a percentage saved is appropriate and when calculating the final decimal percentages rate.
    • Remember to reset the appropriate value(s) to their initial values for each iteration of the bisection search.
    
Examples

Enter the starting salary: 150000
Best savings rate: 0.4411
Steps in bisection search: 12
Enter the starting salary: 10000
It is not possible to pay the down payment in three years

"""

#input
annual_salary=float(input("Enter the starting salary:"))
print("Best savings rate:")
print("Steps in bisection search:")
print("the cost of the house you are saving for is £1M.")


# portion_saved=float(input("Enter the percent of your salary to save, as a decimal: ")) 


# values

total_cost=float(1000000)
portion_deposit = 0.20 
monthly_salary = ((annual_salary/12)+(semi_annual_raise/6))                                                            
deposit = (total_cost/portion_deposit)                                                                      
current_savings=0                                                                            
r = 0.4
months_required =0
interest = (current_savings*r/12)
semi_annual_raise = annual_salary *0.07

#sum

while(current_savings < deposit):
    current_savings+=(monthly_salary+interest)
    months_required+=1
print("Number of months: " , months_required)
