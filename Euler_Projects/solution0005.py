#why do I feel like this is fairly easy
# are we using primes? like why not.
# primes below 20...

#print(2*3*4*5*6*7*8*9*10)
#print(2*3*5*7)
#print(8*9*5)

#this is a question of least common multiple.
#and from memory you remove duplicates of prime factors, the most number of those primes that's found in that number

#print(6*7*8*9*10)

#print(8*5*9*7) #finally lol
#so for numbers up to 20

#print(16*9*5*7*11*13*17*19)

#now how to write that in code.
#I swear there has to be a LCM function that exists lmao

import math
print(math.lcm(4,5,6,9,15,18))

numbers = list(range(1,21))
print(math.lcm(*numbers))