#instead of looking for the largest prime, find the smallest prime that divides the big number and return the answer when it is divided by that number

# x is prime if all the numbers below it can't divide x
## make a list of prime numbers using % modulo sign
#nubers_under_100 = list(range(1,100))

#print(nubers_under_100)

#for x in nubers_under_100:
#    if x % x?? == 0:

#The question said largest prime not largest factor, therefore square root the number and starting dividing it by primes smaller than the answer
# could you start with the biggest prime smaller than it's square root?

import sympy
n = 600851475143
factors = list(sympy.factorint(n))
print("The largest prime is", factors[-1])