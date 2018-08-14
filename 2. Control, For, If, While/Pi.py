from math import sqrt

denom = sqrt(2)
saved = 1
#print ("Kinda doing something")

while True:
  denom = (sqrt(2+denom))
  next_term = 2/denom
  saved = saved * next_term  
    
  if next_term == 1:
    pi = 2*(2/sqrt(2))*saved
    #print (round(pi,3))

    break

print ("The approximation of pi is: %.3f" % (round(pi,3)))  
radius = int(input("What is the radius of your circle? "))  

area = pi*(radius**2)

print ("The area of your circle is: %.3f" % area)

