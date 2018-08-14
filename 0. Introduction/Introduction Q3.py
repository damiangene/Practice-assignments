w1 = int(input("Enter width 1: "))
w2 = int(input("Enter width 2: "))
h1 = int(input("Enter height 1: "))
h2 = int(input("Enter height 2: "))
ppm = int(input("What is the price per meter of fence? "))

fence_perimeter = ((h1*w1)-(h2*w2))
fence_cost = fence_perimeter * ppm

print ("The total fence required is %dm" % (fence_perimeter))
print ("The total cost of the fence is R%d" % (fence_cost))

