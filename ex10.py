"""
Task 1

FizzBuzz has been used as a common challenge during programmer interviews, it requires the
interviewee to write code that prints the numbers between 1 and 100 with the following rules:

•If a number is divisible by 3, print “Fizz”
•If a number is divisible by 5, print “Buzz”
•If a number is divisible by both 3 and 5, print “FizzBuzz”
•Otherwise, print the number

Implement a function that will work through FizzBuzz for the specified number range. Your program
should ask the user for a high and low value before running the function.

Save your program as ex10.py.

"""

#should ask the user for a high and low value before running the function.
#value = input(int(Enter a value betwwen 0(low) and 100(high)))


#function
def FizzBuzz (low,high):
    for num in range(low,high):
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
             print("Buzz")
        else:
            print(num)

FizzBuzz(1,100)
