#instead of looking for the largest prime, find the smallest prime that divides the big number and return the answer when it is divided by that number

# x is prime if all the numbers below it can't divide x
# make a list of prime numbers using % modulo sign
nubers_under_100 = list(range(1,100))

print(nubers_under_100)

for x in nubers_under_100:
    if x % x?? == 0: