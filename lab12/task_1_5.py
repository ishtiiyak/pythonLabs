#########################
####### task 1  #########
#########################
# i=0
# num =eval(input('enter a number '))
# while(i<=num):
#     print(f'{i}\t{i**2}')
#     i=i+1


#########################
####### task 2  #########
#########################

# def fact(num):
    
#     if(num>0):
#         i=1
#         fact=1
#         while (i<=num):
#           fact*=i
#           i=i+1
#         return fact

# num =eval(input('enter a number '))
# print(f'{fact(num)}')        
      
#########################
####### task 3 #########
#########################     

# num =1
# count=0
# sum=0

# while(num!=0):
#     num =eval(input('enter a number '))
#     count+=1
#     sum+=num
# count-=1
# avg=sum/count
    
# print(f'{count}  {avg}')   
   
   
   
#########################
####### task 4 #########
#########################         
# steps=0
# num =eval(input('enter initial value '))
# while(num!=1):
#     steps+=1
#     if(num%2==0):
#         num=num/2
#     elif(num%2!=0):
#         num=(num*3)+1
#     print(f'next  value is {int(num)}')
    
# print(f'total steps are {steps}')    
          
  
#########################
####### task 5 #########
######################### 

steps=0
num =eval(input('enter initial value '))
while(num<=2):
    print('please enter greater than 2')
    num =eval(input('enter initial value '))
while(num!=1):
    steps+=1
    if(num%2==0):
        num=num/2
    elif(num%2!=0):
        num=(num*3)+1
    print(f'next  value is {int(num)}')
    
print(f'total steps are {steps}')    
     
        
  