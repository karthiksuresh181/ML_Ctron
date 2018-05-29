def leng(n):
    return {n:len(n)}

def mymap(func, iterable):
    for i in iterable:
        yield func(i)
            

alist = ['hello', 'you', 'there', 'yes', 'yup']
blist = list(mymap(leng, alist) )

print(blist)
