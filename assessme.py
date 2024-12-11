#from functools import reduce

productNames = ["Laptop", "Tablet", "smartphone", "Monitor", "Keyboard"]
productCategories = ["Electronics", "Electronics", "Electronics", "Peripherals", "Peripherals"]
stockLevels = [[300, 250, 200], [500, 450, 400], [700, 650, 600], [400, 350, 300], [1000, 950, 900]]
salesData = [[50, 60, 70, 80, 90, 100], [30, 35, 40, 45, 50, 55], [100, 110, 120, 130, 140, 150], [20, 25, 30, 35, 40, 45], [150, 160, 170, 180, 190, 200]]
prices = [200000, 45000, 150000, 30000, 15000]

productData = list(zip(productNames, productCategories, stockLevels, salesData, prices))
print(productData)

totalStock = list(map(lambda x: sum(x[2]), productData))
print(totalStock)

lowStockProducts = list(filter(lambda x: sum(x[2]) < 900, productData))
print(lowStockProducts)

totalSales = list(map(lambda x: (x[0], sum(x[3])), productData))



def projectedRevenue(products):
    for product in products:
        name = product[0]
        price = product[4]
        revenue = sum(product[3]) * price
        yield(name, revenue)

for name, revenue in projectedRevenue(productData):
    print(f"Product: {name}, Projected Revenue: {revenue}")
