"""
# Task
Read about Pythons built in “input” function:
https://docs.python.org/3/library/functions.html#input
NB
: The behaviour of input has changed significantly between Python 2.x and 3.x, so be sure that
you are looking at information for the correct version.
Using this, write a program that asks the user to fill out the information you printed in ex4.py from
the last worksheet.

Name
Age
Height (specify inches or cm)
Weight (specify pounds of kilograms)
Eye colour
Hair colour

Use if statements to print different outputs for age, height and weight depending on if they are
above or below specific thresholds. Be polite!

Save the work as ex6.py, make regular commits to GitHub
"""
print ("Exercise ex6.py - intro to programming\n")

name = input("Enter your name: ")
print("Your name is", name, ".")

age = int(input("Enter your age: "))
if age > 18:
    print(name, "is", age, "years old.")


height = float(input("Enter your Height(cm):"))
if height > 0:
    print("That's a positive size!")



weight = float(input("Enter your Weight(kg):"))
if weight > 0:
    print("That's a positive weight!")



eyes = input("Eye colour:")
print ("and your eye color is:"+eyes)

hair = input("Hair colour:")
print ("and your hair color is:"+hair)
