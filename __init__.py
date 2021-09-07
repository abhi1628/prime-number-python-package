import math
from math import sqrt

def test_prime(n):
    if n <= 0:
        return -1
    if n > 0 and n < 2:
        return 0
    if (n==2):
        return 1
    if n > 2 and n % 2 == 0:
        return 0
    x = math.floor(math.sqrt(n))
    for x in range(3,x+1,2):
        if(n % x==0):
            return 0
    return 1

def prev_prime(n):
    for i in range(n-1,1,-1):
        if test_prime(i):
            return i
        
def next_prime(n):
    if (n <= 1):
        return 2
 
    prime = n
    found = False
    
    while(not found):
        prime = prime + 1
 
        if(test_prime(prime) == True):
            found = True
 
    return prime

def prime_upto(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p] and sieve[p]%2==1):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

def fillPrimes(chprime, high):
    ck = [True]*(high+1)
 
    l = int(math.sqrt(high))
    for i in range(2, l+1):
        if ck[i]:
            for j in range(i*i, l+1, i):
                ck[j] = False
    for k in range(2, l+1):
        if ck[k]:
            chprime.append(k)

def range_prime(low, high):
    if(low == 1):
        low += 1
    chprime = list()
    fillPrimes(chprime, high)
    prime = [True] * (high-low + 1)
    for i in chprime:
        lower = (low//i)
    
        if lower <= 1:
            lower = i+i
        elif (low % i) != 0:
            lower = (lower * i) + i
        else:
            lower = lower*i
        for j in range(lower, high+1, i):
            prime[j-low] = False
             
             
    for k in range(low, high + 1):
            if prime[k-low]:
                print(k, end=" ")
    print()            

def isSquare(n): 
    sr = (int)(math.sqrt(n)) 
    return (sr * sr == n) 
  
def fib_prime(n):   
    prime =[True] * (n + 1)  
    p = 2
    while(p * p <= n ): 

        if (prime[p] == True) : 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
                  
        p = p + 1
      
    for i in range(2, n + 1) : 
        if (prime[i] and (isSquare(5 * i * i + 4) > 0 or
             isSquare(5 * i * i - 4) > 0)): 
            print(i,"",end="") 


def prime_factor(n):
    num = n                         
    index = 0                       
    t = [2, 3, 5, 7]               
    f = []                         
    while t[index] ** 2 <= n:                 
        if len(t) == (index + 1):
            t.append(t[-2] + 6)     
        if n % t[index]:           
            index += 1             
        else:
            n = n // t[index]       
            f.append(t[index])     
    if n > 1:
        f.append(n)               
    return f