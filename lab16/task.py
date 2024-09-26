# Write a program that will find the average of the numbers inside a list. The list may contain any 
# number of values. In your program, define a list with a few entries as shown in above example, 
# then use a for loop to find the sum of numbers in that list. After the loop, use that sum to find 
# and display the average.
# Note: There is a built-in Python function named as sum() which can be applied on a list to find 
# the sum of elements but at present do not use it and do this by finding the sum by scanning the 
# whole list

#---------- SOLUTION  -----------#


# sum=0
# myList=[12,32,4,5,65,23,67]
# for i in myList:
#     sum+=i
# print(sum)    
# ------------ ---------- ------------ ----------- #


# Write a program that will replace all list entries which are greater than 10 with 10 and negative 
# entries with 0. You have to do it as:
# a. Start the program by defining a list with few entries similar to above task.
# b. Display the complete list.
# c. Use a for loop to scan the complete list. Within for loop you will check if list element 
# is greater than 10 then update that element to 10. Likewise, the entries less than 0
# should be replaced with 0.
# d. Display the complete list after the entries have been update

#---------- SOLUTION  -----------#


# myList=[12,-32,4,5,-65,23,67]
# print(myList)
# for i in range(len(myList)):
#     if(myList[i]>10):
#         myList[i]=10
#     elif(myList[i]<0):
#         myList[i]=0

# print(myList)
    
# ------------ ---------- ------------ ----------- #


# Write a program that will display number of primes in a list.
# Sample Output is:
# List Elements: [5, 6, 8, 12, 4, 13, 100, 5, 21]
# There are 3 prime numbers in above list
# You will do it as:
# 5 | P a g e
# a. Start the program by defining a list with few positive integers similar to the above task.
# b. Scan the list using a for loop.
# c. Within for loop, use another for loop to find whether that list element is prime or not. 
# If it is prime, increment the count variable.
# d. Do not define function to determine if the number is prime or not.
# e. Display the count.

#---------- SOLUTION  -----------#

# count=0
# myList=[12,32,4,6,99,28,77]
# for i in myList:
#     isPrime=True
#     for j in range(2,i):
#         if(i%j==0):
#             isPrime=False
#             break
#     if (isPrime):
#         count+=1

# print(count)
# ------------ ---------- ------------ ----------- #

#---------- SOLUTION  -----------#


# def isPrime(num):
#     isPrime=True
#     for j in range(2,i):
#         if(i%j==0):
#             isPrime=False
#             return isPrime
#     return isPrime  
# count=0      
# myList=[5,32,7,6,99,11,77]
# for i in myList:
#     if(isPrime(i)):
#         count+=1
# print(count)

# ------------ ---------- ------------ ----------- #


# Finding the maximum value in a list
# In this program define a list with a few entries and then program must find and display the 
# maximum value from list entries.
# How to do that:
# Suppose here is our initial list:
# myList=[30,45,33,82,33,42,15]
# The logic to find maximum out of above list goes something like:
# • Start with declaring first value as the maximum value, like: highest=myList[0]
# • Start scanning the array from second entry till the last one; if the current index value is greater 
# than highest declared, update the highest value as:
# if(myList[i])>highest):
# highest=myList[i]

#---------- SOLUTION  -----------#

# myList=[5,32,7,6,99,11,77]
# largest=myList[1]

# for i in range(len(myList)):
#     if(myList[i]>largest):
#         largest=myList[i]

# print(largest)


# ------------ ---------- ------------ ----------- #

#  Update above task so that both the maximum and the minimum value is inside the list is found 
# and displayed. You have to find both values within the same for loop

#---------- SOLUTION  -----------#
myList=[5,32,7,6,99,-11,77]
largest=myList[1]
smallest=myList[1]

for i in range(len(myList)):
    if(myList[i]>largest):
        largest=myList[i]
    if(myList[i]<smallest):
        smallest=myList[i]
print(largest,smallest)

