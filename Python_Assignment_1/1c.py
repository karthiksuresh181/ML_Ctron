def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]

inp = raw_input("Enter a string : ")
print rreverse(inp)
