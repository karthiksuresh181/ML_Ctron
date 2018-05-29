def leng(word):
    if word == '': return 0
    return 1 + leng(word[1:])
        
inp = raw_input("Enter a string: ")
print "The length of the string: ",leng(inp)
