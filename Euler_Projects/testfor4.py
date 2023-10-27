a= 5
b =11
c = a*b
number_str = str(c)
if number_str == number_str[::-1]:
    print(c)
else:
    print("c is a liar")

def compute():
	ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(ans)


if __name__ == "__main__":
	print(compute())