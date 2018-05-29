def findMinimum(l):
    if len(l) == 1:
       return l[0]
    else:
       return min(l[0], findMinimum(l[1:]))

alist = [int(x) for x in input().split()]
print alist

print "Smallest Element: ",findMinimum(listA)
