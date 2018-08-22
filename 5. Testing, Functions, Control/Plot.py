func = "(1/5)*x +2"
for y in range(10,-11,-1):
    
    for x in range(-10,11):
        if round(eval(func)) == y:
            print("o",end = " ")
        elif x == 0 and y == 0:
            print ("+",end = " ") 
        elif x == 0:
            print("|",end=" ")
        elif y == 0:
            print("-",end = " ")
        else:
            print(" ",end = " ")

    print()

