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

annual_salary=float(input("Enter your annual salary:"))                                    
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))     
total_cost=float(input("Enter the cost of your dream home:"))                               

# values
portion_deposit = 0.20 
monthly_salary = (annual_salary/12)                                                            
deposit = (total_cost/portion_deposit)                                                                      
current_savings=0                                                                            
r = 0.4
months_required =0
interest = (current_savings*r/12)

# number of months required to save for a depoist.


#sum
while(current_savings < deposit):
    current_savings+=(monthly_salary+interest)
    months_required+=1
print("Number of months: " , months_required)
