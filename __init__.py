import math
def test_prime(n):
    if n <= 0:
        return('Number should be greater than zero')
    if n > 0 and n < 2:
        return(n,'is not prime number')
    if (n==2):
        return('2 is a prime number')
    x = math.floor(math.sqrt(n))
    for x in range(3,x+1,2):
        if(n % x==0):
            return (n,'is not a prime number because',(n//x),'times',x,'=',n)
    return (n,'is a prime number')
