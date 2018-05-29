def app(n):
    return n+'s'

def mymap(func, iterable):
    for i in iterable:
        yield func(i)
            

alist = ['hello', 'you', 'there', 'yes', 'yup']
blist = list(mymap(app, alist) )

print(blist)
