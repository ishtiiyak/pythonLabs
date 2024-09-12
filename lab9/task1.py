from ast import For


a=eval(input('enter a number   '))

for i in range(a):
    print(f'{i+1}\t{(i+1)**2}')