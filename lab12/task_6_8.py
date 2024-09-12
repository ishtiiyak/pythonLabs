#########################
####### task 6 #########
#########################

# num =eval(input('enter a number '))
# count=0
# while(num!=0):
#     unit=num%10
#     num=num//10
#     if(unit==0):
#         count+=1
        
# print(f'count is {count}') 

#########################
####### task 7 #########
######################### 

# def isPrime(num):
#     isPrime=True
#     i=2
#     while(i<num):
#         if(num%i==0):
#             isPrime=False
#             return isPrime
#         i+=1
# x =eval(input('enter a positive number '))
# num=x+1
# while(isPrime(num)==False):
#     num+=1
# print(f'next prime is {num}')


#########################
####### task 8 #########
######################### 

def isPrime(num):
    isPrime=True
    i=2
    while(i<num):
        if(num%i==0):
            isPrime=False
            return isPrime
        i+=1
    return isPrime    
x =eval(input('enter a positive number '))
j=2
while(j<=x):
    if(isPrime(j)==True):
        print(j)    
    j+=1
    
