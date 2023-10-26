import sympy

# Check if a number is prime
number = 578679
is_prime = sympy.isprime(number)
print(f"{number} is prime: {is_prime}")

# Generate a list of prime numbers up to a certain limit
limit = 50
primes = list(sympy.primerange(1, limit))
print(f"Prime numbers up to {limit}: {primes}")

# Prime factorization of a number
n = 6076879879
factors = sympy.factorint(n)
print(f"Prime factorization of {n}: {factors}")
