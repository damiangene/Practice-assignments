def input_check():
    n = int(input("Select a starting number: "))
    if n <= -6 or n >= 2:
        input_check()

    else:
        for numbers in range(n,n+41,7):
            print (numbers)

input_check()