


# Write a function that selects a random number and then asks the user to guess what that number is. 
# They should be told if they are higher or lower than the result, track the number of guesses they take to get the correct value. 
# If they do not guess correctly, ask them again until they do.




from random import randint
print(randint(0, 100))	
		
		
def my_function():
  print("try guess the number..")
  
if randint == 0: 
	print("answer is to low")
	print("guess again..")
elif randint == 100:
	print("answer is to high")
	print("guess again..")
else:
	print("answer is correct")

my_function()	
