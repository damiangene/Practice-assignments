def input_check():
    n = int(input("Select a starting number: "))
    if n <= -6 or n >= 93:
        input_check()

    else:
        for numbers in range(n,n+7):
            print (numbers, end =" ")

input_check()
