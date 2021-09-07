### Summary:
* [This is an efficient prime number tester program created to check if the given number is a prime number or not.] 
* [The file is availabe on https://pypi.org/project/abhiprime/#files]

### Steps to use:
* [Open the code editor like jupyter or google colab where you can install packages. Like in Jupyter type-] 
```
!pip install abhiprime

```
* [One can also use command prompt. Open the path where python is installed and type-] 
```
pip install abhiprime

```
* [Once installation is done open your IDE and type-]

``` 
import abhiprime 
```
or 

```
import abhprime as ap
```
* [Press enter] 
* [Now type- abhiprime.test_prime(any number which you want to check)] 
* [If you are using alias name for abhiprime then type- ap.test_prime(any number which you want to check)]
* [If you get ModuleNotFoundError (It may happen if you install via command prompt), then make sure that path specified for python is correct and is added in environment path variable.]

#### If you are already using abhiprime then please upgrade it, using 
```
$ pip install --upgrade abhiprime

```

#### If upgradation is throwing error, then uninstall the previous version and install the latest version.

* After upgradation, type
```
import abhiprime as ap
from abhiprime import *

```
* Now you can use it to check the following operations:

```
ap.test_prime(n)- This is an efficient prime number tester program created to check if the given number is a prime number or not.
ap.prev_prime(n)- used to give the just previous prime number value from the given number n.
ap.next_prime(n)- used to give the just next prime number value from the given number n. 
ap.prime_upto(n)- gives a list of prime numbers upto the given number n.
ap.range_prime(n,m)- gives a list of prime numbers between numbers n and m.
ap.fib_prime(n)- gives a list of numbers which are prime and fibonacci also.
ap.prime_factor(n)- gives the prime factors of any number
```
