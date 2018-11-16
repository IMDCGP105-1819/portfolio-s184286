

def fib(n):
	for n in range(0,20):
		if(n==0):	# <-- base case
			return n
		else:
			return fib(n-1)+fib(n-2)  # <-- recursive step
		print(n)










