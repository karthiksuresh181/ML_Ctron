def myfilter(dele, lst):
    return [x for x in lst if x[0] % x[1] == 0]

alist = [(2,2),(3,5),(4,2),(6,3),(7,3)]
rlist = myfilter(1,alist)
print("The Given List of Tuples: ",alist)
print("The Resulting List of Tuples: ",rlist)
