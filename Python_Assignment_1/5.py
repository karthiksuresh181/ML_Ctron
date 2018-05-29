s = 'abcd'
t = (10, 20, 30)
u = (-1,-2,-3)
al = [1,2,3]

def shortest_sequence_range(*args):
     return range(len(sorted(args, key=len)[0]))

g = ((s[i], t[i], u[i], al[i])
         for i in shortest_sequence_range(s,t,u,al) )

print("Inbuilt Zip(): ",list(zip(s,t,u,al)))

print("\nUser Defined Zip():")
for item in g:
        print(item)
