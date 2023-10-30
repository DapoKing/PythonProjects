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

print(generate_primes(900000)[10001])