from functools import reduce

product_name = ["Laptop", "Tablet", "smartphone", "Monitor", "Keyboard"]
product_categories = ["ELectronics", "Electronics", "ELectronics", "Peripherals", "Peripherals"]
stock_levels = [[300, 250, 200], [500, 450, 400], [700, 650, 600], [400, 350, 300], [1000, 950, 900]]
sales_data = [[50, 60, 70, 80, 90, 100], [30, 35, 40, 45, 50, 55], [100, 110, 120, 130, 140, 150], [20, 25, 30, 35, 40, 45], [150, 160, 170, 180, 190, 200]]
prices = [200000, 45000, 150000, 30000, 15000]

b = list(zip(product_name, product_categories, stock_levels, sales_data, prices))
print(b)

d = list(map(lambda x: sum(x[2]), b))
print(d)

z = list(filter(lambda x: sum(x[2]) < 900, b))
print(z)

total_sales = list(map(lambda x: (x[0], sum(x[3])), b))


def projected_revenue(products):
    for i in products:
        name = i[0] 
        price = i[4]
        revenue = sum(i[3]) * price  
        yield (name, revenue)

for name, revenue in projected_revenue(b):
    print(f"Product: {name}, Projected Revenue: {revenue}")
