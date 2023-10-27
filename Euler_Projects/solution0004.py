#palindrome numbers... is there a way for python to see if a string is the same even if reversed? how do you even reverse a string?
#is there anything unique about palindrome numbers prime factorization that could help?
#and i need to find the largest from two 3 digit numbers, safe to say it is less than a million lol

#    reversed_str = number_str[::-1]

#for ??? x ???  
# multiplying each 3 digit number with itself would be too long

palindrome_numbers = []
for a in range(100, 1000):
    for b in range(100, 1000):
        c = a * b
        number_str = str(c)
        if number_str == number_str[::-1]:
            palindrome_numbers.extend([a,b,c])
            #print(palindrome_numbers) #lol they are all strings

max_palindrome = max(palindrome_numbers)

print("The maximum palindromic number is:", palindrome_numbers[-3], "X", palindrome_numbers[-2], "=", max_palindrome)

#wow that was fun and challenging, learnt a lot!