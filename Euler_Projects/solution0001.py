"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
The sum of these multiples is 23

Find the sum of all the multiples of below 1000 """

#list all numbers

numbers_list = list((range(1,1000)))
#print(numbers)

#this is the list of numbers I want to add
add = []
#if statement for if they are divisible by 3 else if 5
for i in numbers_list:
    if i % 3 == 0:
        add.append(i)
        #print(add)
    elif i % 5 == 0:
        add.append(i)
        #print(add)

#need to make sure this doesn't include duplicates.

#add it to a new list or append it

#then finally add all the elements together
total = sum(add)
print("The summation of the numbers divisible by 3 or 5 is", total)