def printPattern(i, j=0):
    print("*")
    print("\n")
    print("\n***** ")
    print("\n")
    print("\n***")
    print("\n")
    print("\n*****")
    print("\n")
    print("\n*")
    j += 1
    if j < i:
        printPattern(i, j)
    else:
        return  
    
printPattern(2)