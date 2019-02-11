"""
Task 3

Write an application that allows you to calculate the cost of a trip.

Implement a function called hotel_cost that takes one argument, nights, as input. The hotel costs
£70 per night – so return a suitable value.

Implement a function called plane_ticket_cost that accepts a string, city, and a float, class, as inputs.

The function should handle the following locations, returning their associated round trip costs that
are multiplied by the class amount.

“New York”: £2,000
“Auckland”: £790
“Venice”: £154
“Glasgow”: £65


The class multiplier starts at 1 for economy and goes up in .3 steps: 1.3 = premium economy, 1.6 =
business class and 1.9 = first class.

Then implement the rental_car_cost function with an argument called days. The function should
calculate the cost of hiring a car with the following considerations:

•Every day of car hire costs £30
•If you rent the car for more than 7 days, you get £50 off your total
•If you rent the car for more than 3 days, you get £30 off your total
    oThese two discounts cannot be applied at the same time.

Define a function total_cost which accepts two arguments; city and days. It should call the other
functions and return the sum of the cost of the trip.

Save the file as the next numeric ex value and commit to GitHub.

"""

nights = int(input("how many number of nights stay?"))

def hotel_cost(nights):
    nights*70
    print("number of nights",nights) 
    
hotel_cost(nights)


city=str(input("select your destination: New york, Auckland, Venice, Glasgow: "))

def plane_ticket_cost(city, _class):        # the function should handle the following locations, returning thier associated round trip costs that are multiplied by the class amount.
	
    if city=='New york':
	    plane_ticket_cost = 2000.00
    elif city=='Auckland':	
	    plane_ticket_cost = 790.00
    elif city=='Venice':
	    plane_ticket_cost = 154.00
    elif city=='Glasgow':
	    plane_ticket_cost = 65.00


# the class multiplier starts at 1 for economy and goes up in 3 steps: 1.3 premium economy 1.6 = business class and 1.9 = first class.		

_class=float(input("Select your Travel Class: 1=Economy, 1.3=Premium Economy, 1.6=Business Class, 1.9=First Class: "))   
	
if _class=='1':
	print("Economy Travel Class selected")
elif _class=='1.3':	
	print("Premium Economy Travel Class selected")
elif _class=='1.6':
	print("Business Class Travel Class selected")
elif _class=='1.9':
	print("First Class Travel Class selected")

plane_ticket_cost(city, _class)
  

days=float(input("enter how many number of days car hire required: "))

def rental_car_cost(days):		# Every day of car hire costs £30
    		
    if days > 0:
	    print(days * 30)
    elif days > 3:
	    print(days * 30 -30.00)			# If you rent the car for more than 3 days, you get £30 off your total
    elif days > 7:
	    print (days * 30 -50.00)		# If you rent the car for more than 7 days, you get £50 off your total
											# These two discounts cannot be applied at the same time.

rental_car_cost(days)

def total_cost(city,days):		# accepts two arguments, city and days.
                                # it should call the other functions and return the sum of the cost of the trip.
    
    print("the Hotel Cost is:", hotel_cost(nights))
    print("the Plane Ticket Cost: ", plane_ticket_cost(city, _class))
    print(" Rental Car Cost:", rental_car_cost(days) )
    print("Choice of city:", city)
    print("for ",days, "no of Days")
    print("Travelling in", _class,  )   
		
total_cost(city,days)



