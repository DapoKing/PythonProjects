#my first tboughts are to create an algorithm for the Fibonacci sequence, if there isn't already

#using indexes to change and append lists in a while loop.

#the question is to sum the even valued terms. 

#instead I can just sum the 4th term in an index

#the first even number is in position [1] and the next [5] 

# So I'd just need to keep adding those numbers using sum() to a list that's largest number is less than 4 million

# that less than 4 million part could be included in the while loop

def fibonacci(n):
    fibonacci_list = [1,2]
    while len(fibonacci_list) < n and fibonacci_list[-1] <4000000:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list
result = fibonacci(36)
even_list = result[1::4]
    
    
print(result, sum(even_list))

#this will be needed
#while fibonacci_list[-1] <4000000:
#    even_list = fibonacci_list[1::4]
#    sum(even_list)


