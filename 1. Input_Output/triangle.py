import math
a = float(input("Enter the length of side 1"))
b = float(input("Enter the length of side 2"))
c = float(input("Enter the length of side 3"))

s = ((a + b + c)/2)
area = (s*(s-a)*(s-b)*(s-c))
area = math.sqrt(area)

print ("The area of your triangle is %.2f" % (area))