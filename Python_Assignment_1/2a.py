def sq(n):
    return n*n

def mymap(func, iterable):
    for i in iterable:
        if i %2 != 0:
            yield func(i)
            
n = int(input("Enter the value of n: "))
alist = range(n)
blist = list(mymap(sq, alist) )

print(blist)
