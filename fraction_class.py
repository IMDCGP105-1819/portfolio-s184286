


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

    def add(self, other):  
        return self.num + self.denom  # addition (returns a new fraction representing the result of the addition)


    def sub(self,other)  
        return self.num - self.denom  # substraction (returns a new fraction representing the result of the substraction)

    def multiply(self,other)  
        return self.num * self.denom  # multiplication (returns a new fraction representing the result of the multiplication)

    def divide(self,other)  
        return self.num / self.denom  # division (returns a new fraction representing the result of the division)    

    def inverse(self,other)  
        inverse x!y
        return self.num ! self.denom  # inverse (returns a new fraction representing the result of the inverse)	

	try:
		print(fraction)
	except:
		print("ValueError")
	except:
		print("NameError")


# instance of the fraction class

fraction = Fraction(2, 3)
fraction.add(Fraction(1,2))


# calling the math functions

add_fraction = fraction.add(self.num,self.denom)
minus_fraction =fraction.sub(self.num, self.denom) 
multiply_fraction =fraction.multiply(self.num, self.denom)
division_fraction = fraction.divide(self.num, self.denom)
inverse_fraction = fraction.inverse(self.num, self.denom)



printing to output..



print("Sum of Addition:" .add())
print("Sum of Subtraction:" .sub())
print("Sum of Division:" .multiply())
print("Sum of Multiply:" .divide())
print("Sum of Inverse:" .inverse())
