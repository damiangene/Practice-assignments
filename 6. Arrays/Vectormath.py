from math import sqrt as sqrt
def add(a,b):
    c = []
    i = 0
    for _ in a:
       c.append(a[i]+b[i])
       i += 1

    return c

def product(a,b):
    c = 0
    i = 0
    for _ in a:
       c += (a[i]*b[i])
       i += 1

    return c

def norm(a):
    c = 0
    i = 0
    for _ in a:
       c += ((a[i])**2)
       i += 1
    
    return (sqrt(c))
     

vector_a = (input("Enter vector A: ")).split()
vector_b = (input("Enter vector B: ")).split()

vector_a = [ int(x) for x in vector_a ]
vector_b = [ int(x) for x in vector_b ]

print ("A+B = {}".format(add(vector_a,vector_b)))
print ("A.B = {}".format(product(vector_a,vector_b)))
print ("|A| = {:0.2f}".format(norm(vector_a)))
print ("|B| = {:0.2f}".format(norm(vector_b)))
