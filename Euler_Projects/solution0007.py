#finding the 10001th prime
list = []
for i in range(1,9,2):
    if i % 5 == 0:
        list.append(i)

print(list)

def generate_primes(limit):
    primes = []
    for number in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes

print(generate_primes(120000)[10000])

#his answer
import eulerlib, itertools


# Computers are fast, so we can implement this solution by testing each number
# individually for primeness, instead of using the more efficient sieve of Eratosthenes.
# 
# The algorithm starts with an infinite stream of incrementing integers starting at 2,
# filters them to keep only the prime numbers, drops the first 10000 items,
# and finally returns the first item thereafter.
def compute():
	ans = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None))
	return str(ans)
print(compute())