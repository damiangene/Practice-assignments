def input_check():
    n = int(input("Select a starting number: "))
    if n <= -6 or n >= 2:
        input_check()

    else:
        for rows in range(6):
            for numbers in range(n,n+7):
                print ("{:>3}".format(numbers), end =" ")
            n = n+7
            print()
input_check()