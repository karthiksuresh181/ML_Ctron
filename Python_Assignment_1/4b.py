def myreduce(func, seq):
	maxi = func(seq)
	return maxi

alist = [23,345,45,567,67,45,2]
print("The Given List: ", alist)
print("The Maximum in the list: ","".join(map(str, alist)))



x = [1,3,5]
r = int("".join(map(str, x)))
print(r)
