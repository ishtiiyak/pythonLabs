# a=open(r'C:/Users/BUZZ TECH/pythonLabs/text/text.txt','r')
# f=a.readlines()
# print(f)
# y=open(r'C:/Users/BUZZ TECH/pythonLabs/text/text.txt','w')
# z=y.write('My')
# print(z)

# Define the dictionary with goods and their prices
goods_prices = {
    "Apple": 0.50,
    "Banana": 0.30,
    "Milk": 1.20,
    "Bread": 1.00,
    "Eggs": 2.50
}

# Function to write goods and prices to a file
def goods_prices(filename, goods_prices):
    file = open('C:/Users/BUZZ TECH/pythonLabs/text/text.txt', 'a')
    try:
        for good, price in goods_prices.items():
            file.write(f"{good}: ${price:.2f}\n")
    finally:
        file.close()







def display_text(filename):
    try:
        file = open(f'C:/Users/BUZZ TECH/pythonLabs/text/{filename}', 'r')
        t=file.read()
        
        print(f'{t}')
    except FileNotFoundError as notFount:
        print(notFount)
    except PermissionError as permiss:
        print(permiss)
    except KeyboardInterrupt as keybaod:
        print(keybaod)
    except Exception as excp:
        print(excp)
    finally:
        print('text.txt')     
# file =input('please enter file name ')





def generate_invoice(customer_name, items):
    try:
        file = open('C:/Users/BUZZ TECH/pythonLabs/text/text.txt', 'a')
        total_cost = 0
        invoice=f"Invoice for {customer_name}\n"
        invoice+=("-" * 30)
        for item, cost in items.items():
            invoice+=(f"{item}: ${cost:.2f}\n")
            total_cost += cost
        invoice+=("-" * 30)
        invoice+=(f"Total: ${total_cost:.2f}")
    
        file.write(invoice)
    except:
        print('error')
    finally:
        file.close()

# Example usage
items={'apples':5.50, 'bread':2.75, 'milk':3.25, 'cheese':4.50}

##  task one
# goods_prices("goods_prices.txt", goods_prices)

##  task two
# display_text('text.txt')   

##  task three
generate_invoice("John Doe",items )
