


# task 1 - "Fraction class"


# implement a "fraction" class, it should provide the following attributes:
# the class should offer suitable attributes to use the print and float functions. should ensure check that the values provided to _self_ are integers and respond with a suitable error message if they are not.


# inputs:

num = int(input("enter a number:"))
denom = int(input("enter a second number:"))

print("numerator value = ", num) 
print("denome value = ", denom) 

class Fraction:				# implement a "fraction" class, it should provide the following attributes:	
	def __init__ (self, num, denom):
		self.num = num				# data - num(integer)
		self.denom = denom			# data - denom (integer)

 defining math functions

    def addition(self, other):  
        return self.num + self.denom  # addition (returns a new fraction representing the result of the addition)


    def substraction(self,other)  
        minus x-y
        return("..new faction")  # substraction (returns a new fraction representing the result of the substraction)

    def multipilcation(self,other)  
        multiplication x*y 
        return("..new faction")  # multiplication (returns a new fraction representing the result of the multiplication)

    def division(self,other)  
        divide x/y
        return("..new faction")  # division (returns a new fraction representing the result of the division)    

    def inverse(self,other)  
        inverse x!y
        return("..new faction")  # inverse (returns a new fraction representing the result of the inverse)	

	try:
		print(fraction)
	except:
		print("ValueError")
	except:
		print("NameError")





# calling the math functions

add_fraction = fraction.add(self.num,sef.denom)
minus_fraction = 
multiply_fraction =
division_fraction = 
inverse_fraction = 



printing to output..



print("Sum of Addition:")
print("Sum of Subtraction:")
print("Sum of Division:" )
print("Sum of Multiply:" )
print("Sum of Inverse:")
