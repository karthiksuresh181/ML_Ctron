import random

while (True):
    print("\n\n--------Dice Simulator---------\n\n")
    n=int(input("Enter the choice\n1-Roll the dice\n2-Exit\n\nInput --> "))
    if(n==1):print("Dice Value: "+str(random.randint(1,6)))
    else: exit()
