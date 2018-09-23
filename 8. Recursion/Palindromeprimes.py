import sys
sys.setrecursionlimit (30000)
from math import sqrt as sqrt

m = int(input("Enter a starting point: \n"))
n = int(input("Enter an ending point: \n"))
print ("The Palindromic primes are: ")

def palindromeprime(m,n):
    def prime_check(m,base_check):          
        if m % base_check > 0:
            base_check -= 1
            
            if base_check > 1:
                return prime_check(m,base_check)
            
            else:                
                return True
                
        else:
            return False 

    if str(m)[::-1] == str(m):
        if prime_check(m,base_check = int(sqrt(m))) == True:
                print (m)
                m += 1
                palindromeprime(m,n) 

        else:
            m += 1
            palindromeprime(m,n)  

    
    elif (m + 1) <= n:
        m += 1
        palindromeprime(m,n)

palindromeprime(m,n)