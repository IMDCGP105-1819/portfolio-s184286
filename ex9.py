
	
# write a program to calculate the best savings rate, as a function of your starting salary
# bisection search.


annual_salary = float(input("Enter annual salary amount: "))

total_cost=1000000
semi_annual_raise=0.07
monthly_salary = ((annual_salary/12)+(semi_annual_raise/100*6))                                 
down_payment= (total_cost*0.25)                                                                      
current_savings=0                                                                            
r = 0.04

months_required =0
interest = (current_savings*r/12)
months_to_save=36



low=0
high=100000
epsilon = 100
guess= (high + low)/2.0
steps = 0



while abs(current_savings <= down_payment + epsilon) and abs(current_savings >= down_payment - epsilon):
	for i in range(1, months_to_save+1):
		current_savings +=monthly_salary
		current_savings +=(interest/12)
		months +=1
		if month % 6==0:
			current_savings += (current_savings*semi_annual_raise)
		months +=1
	if current_savings < down_payment + epsilon or current_savings < down_payment - epsilon:
		print("..not possible for you to afford the deposit within the time period")
		break
	current_savings =0
	months=0
	for i in range(1, months_to_save+1):
		current_savings += (monthly_salary * guess)
		current_savings += (current_savings * interest/12)
		months+=1
		if months % 6==0:
			current_savings += (current_savings *semi_annual_return)
	if current_savings < down_payment:
		low = guess
	else:
		high = guess
		guess = guess/10000
		steps +=1
		print("Best savings rate: ", round(guess,2))
		print("Steps in bisection:", steps)
		
