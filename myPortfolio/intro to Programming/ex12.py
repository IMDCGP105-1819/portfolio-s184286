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
