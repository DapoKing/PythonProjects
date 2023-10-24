
def fibonacci(n):
    fibonacci_list = [1,2]
    while len(fibonacci_list) < n and fibonacci_list[-1] <4000000:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list
print(fibonacci(35))