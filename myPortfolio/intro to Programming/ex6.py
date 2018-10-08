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

a=input("Enter your Name:")
print ("hi!"+a)

b=input("Enter you Age please:")
print ("sir", "your age is:"+b)


c = input("Height:")
print (a, "and your Height is:"+c)

d = input("Weight:")
print (a, "and your Weight is:"+d)


e = input("Eye colour:")
print (a, "and your eye color is:"+e)

f = input("Hair colour:")
print (a, "and your hair color is:"+f)




print ("your height is:   " +c)
print ("your weight is: " +d)
print ("your eye colour is:   " +e)
print ("your hair color is:   " +f)
