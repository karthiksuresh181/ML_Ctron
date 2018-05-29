def mx(maxi, nxt):
    if nxt > maxi:
        return nxt
    else:
        return maxi

def myreduce(func, seq):
	maxi = seq[0]
	for nxt in seq[1:]:
		maxi = func(maxi, nxt)
	return maxi

alist = [23,345,45,567,67,45,2]
print("The Given List: ", alist)
alist = sorted(alist)
print("The Maximum in the list: ",myreduce(mx, alist))

