    # write a program that will help you calculate how long it will take (months) to save up for a deposit,

    # inputs

annual_salary=float(input("Enter your annual salary:"))                                    
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))     
total_cost=float(input("Enter the cost of your dream home:"))                               

    # values

monthly_salary = (annual_salary/12)                                                            
deposit = (total_cost/portion_saved)                                                                      
current_savings=0                                                                            
r = 0.04
months_required =0
interest = (current_savings*r/12)

    # sum

while(current_savings < deposit):
    current_savings+=(monthly_salary+interest)
    months_required+=1
print("Number of months: " , months_required)
