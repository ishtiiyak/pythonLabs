from ast import For



# num=eval(input('enter a number   '))

# for i in range(num+1):
#     print('*'*i)






# num=eval(input('enter a number   '))

# for i in range(num,0,-1):
#     print('*'*i)






# num=eval(input('enter a number   '))
# count =1
# for i in range(num,0,-1):
#     print('t'*(i-1))
#     print('*'*count)
#     count+=1






countEven =0
countOdd =0
for i in range(10):
    num=eval(input('enter a number   '))
    if(num%2==0):
        countEven+=1
    elif(num%2!=0):
        countOdd+=1


print(f'{countEven} {countOdd}')



