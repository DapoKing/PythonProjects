a= 5
b =11
c = a*b
number_str = str(c)
if number_str == number_str[::-1]:
    print(c)
else:
    print("c is a liar")