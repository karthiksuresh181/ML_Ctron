import random
x=random.randint(1,100)

while(True):
    n=int(input("\nGuess the Number: "))
    if(n==x):
        print(str(x)+" is Correct")
        exit()
        
    elif((n-x)>0):
        print("Number is High")
        
    else:print("Number is Low") 
