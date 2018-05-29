def myfilter(dele, lst):
    return [x for x in lst if x[0].isalpha()]

alist = ['hello', '1you', '2there', 'yes', 'yup']
rlist = myfilter(1,alist)
print("The Given List: ",alist)
print("The Resulting List: ",rlist)
