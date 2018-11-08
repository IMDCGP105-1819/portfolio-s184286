# replace these with your own values!

"""
When we use a statement with a single equal (=) sign, we are assigning some data to a variable – we are giving it a name. What happens if you use two equal signs next to each other (==)? 

Python provides several built-in data types: 

• boolean 
  o represented by True and False and nothing else. 
• int, float and complex numbers. 
• strings  
  o Everything we have used in our “print” statements are strings 
  o We can assign strings to variables! 
   test_string = “this is a string” 
  
There are several others, but they can wait for the time being. 

Create a new file and save it as ex4.py – enter the following code:
"""

my_name = 'R Miah'

my_age = 36

my_height = 64

my_weight = 112

my_eyes = 'Brown'

my_hair = 'Black'

is_heavy = my_weight > 212



print(f"Let's talk about {my_name}.")



print(f"He is {my_height} inches tall.")

print(f"He's {my_weight} pounds heavy.")

print(f"It is {is_heavy} that he is overweight.")

print(f"He's got {my_eyes} eyes and {my_hair} hair.")



total = my_age + my_height + my_weight

print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}")

# Write some variables that convert from inches and pounds into centimetres and kilograms, do the math in Python – don’t hard code the values


x = int(input("please enter a number(decimal): "))
print("your number is", round(x / 2.54,2), "inches")
print("your number is", round(x / 2.205,2), "kilograms") 

