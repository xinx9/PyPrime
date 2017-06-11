import math
prime = []
def isPrime(x):
    if not x % 2 ==0 and x > 2:
        return all(x % i for i in range(3, int(math.sqrt(x))+1))
def isPrimeToInt(x):
    if(isPrime(x) == True):
        return x
def isPrimeToStr(x):
    if(isPrime(x)==True):
        return "%d Is a Prime"%x
    else:
        return "%d Is not a Prime"%x
print(" This program finds prime numbers")
decision = int(input("\tIf you want all primes ENTER: 1(default)\n\tIf you want to find a specific prime ENTER: 2\n\t\tEnter #: "))
num = int(input('\t\tEnter #: '))
if(decision != 2):
    for i in range(num):
        prime.append(isPrimeToInt(i))
    prime = list(filter(None, prime))
    print("\nHere are your Primes\n%r"%prime)
else:
    print("\n" + isPrimeToStr(num))
