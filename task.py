

## Main programme

print('Welcome to the inventory MAnagment System \n\
1. ADD item \n2.Display inventory \n3.Sell item \n4.veiw earnings \n5.Apply discount \n6.exit'      
)
inventory=[]
while(True):
    
    itemName=''
    earnings=0
    quantity=0
    unitPrice=0
    newItem=(itemName,quantity,unitPrice)
    userOption=eval(input('select an option '))
    if(userOption==1):
        itemName=input('enter item name ')
        quantity=eval(input('enter item quantity '))
        unitPrice=eval(input('enter unit price '))
        newItem=(itemName,quantity,unitPrice)
        inventory.append(newItem)
        print('item added succesfully')
    if(userOption==2):
        print('current inventory')
        for i in range(len(inventory)):
            for j in range(3):
                print(f'item: quantity: rate per item {inventory[i][j]} ',end='')
            print(',')    

    if(userOption==3):
        itemName=input('enter item name')
        quantity=eval(input('enter item quantity'))
        earnings+=quantity*unitPrice
        print(f'{quantity } {itemName} sold total cost {quantity*unitPrice}')
    if(userOption==4):
        print(f'total earnings is {earnings}')    

    if(userOption==5):
        print('discount')
        for i in range(len(inventory)):
            if(inventory[i][1]<5):
                inventory[i][2]-=(inventory[i][1]*10)/100
                print(f'{inventory[i][0] } has 10 percent discount and price is {inventory[i][2]}')

    if(userOption==6):
        print('thanks for choosing us')
        exit()    

