def decimal_to_bukiyip(number):
    
    i = 0
    test = 3
    answer = ""

    while test > 2:
        test = number/(3**i)
        i += 1
    
    i -= 1
   
    while i >= 0:
        
        base3 = int(number//(3**i))
        number = number%(3**i)
        i -= 1
        answer = answer + str(base3)
        
    return answer


def bukiyip_to_decimal(number):
    number_as_list = [int(i) for i in str(number)]
    length = len(number_as_list)-1
    answer = 0

    for number in number_as_list:        
        tmp = number*(3**length)
        length -= 1
        answer += tmp

    return answer


def bukiyip_add(a, b):
    a = bukiyip_to_decimal(a)
    b = bukiyip_to_decimal(b)
    c = a + b

    c = decimal_to_bukiyip(c)
    return c

def bukiyip_multiply(a, b):
    a = bukiyip_to_decimal(a)
    b = bukiyip_to_decimal(b)
    c = a * b

    c = decimal_to_bukiyip(c)
    return c

options = {"d": decimal_to_bukiyip, "b": bukiyip_to_decimal,
            "a": bukiyip_add, "m": bukiyip_multiply, "q": exit}

print ("**** Bukiyip test program ****\n")
print ("Available commands:")
print ("d <number> : convert given decimal number to base-3.")
print ("b <number> : convert given base-3 number to decimal.")
print ("a <number> <number> : add the given base-3 numbers.")
print ("m <number> <number> : multiply the given base-3 numbers.")
print ("q : quit")

user_input = input("")

if len(user_input.split()) == 3:
    func, var1, var2 = user_input.split()
    var1 = int(var1)
    var2 = int(var2)
    answer = options.get(func)(var1,var2)
    print (answer)
    
elif len(user_input.split()) == 2:
    func, var1 = user_input.split()
    var1 = int(var1)
    answer = options.get(func)(var1)
    print (answer)

elif user_input == "q":
    options.get(user_input)()

else:
    exit()
