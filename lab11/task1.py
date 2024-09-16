######################################################################
############################### LAB 12 ###############################
######################################################################


##############################
########### TASK 1 ###########
##############################
sum=0
product=1
for i in range(3):
    for j in range(3):
        x=eval(input(f'enter A{i+1}{j+1} '))
        sum+=x
        product*=x

print(f'sum of all numbers is {sum} and product is {product}')

##############################
########### TASK 2 ###########
##############################
x=eval(input('enter a number'))
sum=0
for i in range(1,x+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    sum+=(1/fact)
print(sum)

##############################
########### TASK 3 ###########
##############################
def fact(num):
    fact=1
    for j in range(1,num+1):
        fact*=j
    return fact
    
def mySeries(num):
    sum=0
    for i in range(1,num+1):
        sum+=1/fact(i)
    return sum
        
print(mySeries(x))      
        
        




