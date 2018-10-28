"""
Task 1

Explore what happens if you try to mutate a list while iterating over it (using a for loop), what 
happens when you run the following function? What is your expected result and what do you get?

def remove_dups(L1, L2): 
	for e in L1: 
		if e in L2: 
			L1.remove(e) 
L1 = [1, 2, 3, 4] 
L2 = [1, 2, 5, 6] 
remove_dups(L1, L2)

Modify the function so that it works as you would expect it to. This happens because Python uses an 
internal counter to keep track of the index in a loop, when we modify the length of a list inside a for 
loop, Python never updates that internal counter.

"""