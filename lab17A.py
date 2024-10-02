import random
# a = [7,3,6,10,-8]
# b=[2,3]
# # print(a.index(max(a)))

# a.remove(3)

# a.pop(1)
# a.insert(0,223)
# a.append(23)
# a.extend(b)
# print(a)

##-------  TASK ONE ---------------
 
# a = [7,3,6,10,6,7,-2,7,5,-8,23,112,-22,3,6,-5,7,5,10,-20]
# print(a.index(max(a)))

# b=sorted(a)
# lessThanSeven=b.index(7)

# print(b)
# count=b.count(7)
# secondLargest=b[len(b)-2]

# print(f'numbers less than 7 are {lessThanSeven} and greater than seven are {len(b)-(lessThanSeven+count)} second largest number {secondLargest} is at index {a.index(secondLargest)}')

# a[a.index(min(a))]=max(a)

# print(a)

##-------  TASK TWO ---------------
# Write a program that will ask user to enter numbers and will then find and display the average, 
# the highest and the lowest values. User can enter as many numbers as he wants and will enter 
# 1 to end the process. Use one while loop to take in the entries as shown above and then use 
# only one for loop to calculate the three outputs.

# a=[]
# while(True):
#     num=eval(input('enter numbers '))
#     if(num==1):
#         break
#     a.append(num)
# smallest=a[0]
# largest=a[0]
# for i in range(len(a)):
#     if(a[i]<smallest):
#         smallest=a[i]
#     if(a[i]>largest):
#         largest=a[i]    

# print(f'smallest is {smallest} and largest is {largest} and the aaverage is {(largest+smallest)/2}')    


##-------  TASK THREE ---------------


# [3] Write a program that will first create a list of 20 random numbers (1 to 50). One for or while 
# loop will do this part. Then the program should create a new list that will contain all prime 
# numbers in the first list. Using a function isPrime is up to you. 
# Sample Output is: 
# A random List: [5, 16, 28, 12, 44, 13, 40, 35, 21, 37, 24, 31, 
# 27, 13, 34, 19, 41, 33, 29, 34] 
# List of Prime numbers: [5, 13, 37, 31, 13, 19, 41, 29] 

# def isPrime(num):
#     for i in range(2,num):
#         if(num%i==0):
#             return False
#     return True
# a=[]
# primes=[]
# i=0
# while(i<20):
#     rand=random.randrange(1,50)
#     i=i+1
#     a.append(rand)
# for i in a:
#     if(isPrime(i)):
#         primes.append(i)
# print(f'list of random numbers is {a} and primes are {primes} ')  

# a = [7,3,6,10,6,7,-2,7,5,-8,23,112,-22,3,6,-5,7,5,10,-20]
# print(a[15:]) 
# print(a[::-1]) 


##-------  TASK FOUR ---------------

marks=[]

Sum=0

students=eval(input('enter the numebrs of students in class '))
i=0
while(i<students):
    num=eval(input(f'enter marks of student {i+1} '))
    marks.append(num)
    i=i+1
smallest=marks[0]
largest=marks[0] 
failingCount=0  
for i in range(len(marks)):
    Sum+=marks[i]
    if(marks[i]<smallest):
        smallest=marks[i]
    if(marks[i]>largest):
        largest=marks[i]
    if(marks[i]<40):
        failingCount+=1    

# print( f'{smallest}  {largest}  {Sum/len(marks)}  {failingCount}')
print(f'******************************************** * \n\
* Result of Computer Programming-I   * \n\
******************************************** * \n\
* Average Marks: {Sum/len(marks)}      *  \n\
* Failing Students: {failingCount}      *  \n\
* Highest Marks:  {largest} Obtained by Roll No. :{marks.index(max(marks))+1} *  \n\
* Lowest Marks:{smallest} Obtained by Roll No. :{marks.index(min(marks))+1} * \n\
******************************************** * ')