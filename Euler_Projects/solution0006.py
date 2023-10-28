#Sum Square Difference

numbers = list(range(1,101))
squared_numbers = []
total_numbers = sum(numbers)

for num in numbers:
    result = num ** 2
    squared_numbers.append(result)

ans = total_numbers ** 2 - sum(squared_numbers)

print(ans)

### His solution
def compute():
	N = 100
	s = sum(i for i in range(1, N + 1))
	s2 = sum(i**2 for i in range(1, N + 1))
	return str(s**2 - s2)


if __name__ == "__main__":
	print(compute())