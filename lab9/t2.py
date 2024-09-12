from ast import For


num=eval(input('enter a number   '))
limit=eval(input('enter limit   '))
for i in range(limit):
    print(f'{num} x {i+1} = {num*(i+1)}')