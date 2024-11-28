from functools import reduce

product_names = ("Laptop", "Tablet", "Smartphone", "Monitor", "Keyboard")
product_categories = ("Electronics", "Electronics", "Electronics", "Peripherals", "Peripherals")
stock_levels = [
    (300, 250, 200),
    (500, 450, 400),
    (700, 650, 600),
    (1000, 950, 900),
    (400, 350, 300)
]
sales_data = [
    (150, 60, 70, 80, 90, 100),
    (30, 35, 40, 45, 50, 55),
    (100, 110, 120, 130, 140, 150),
    (120, 125, 130, 135, 140, 145),
    (150, 160, 170, 180, 190, 200)
]
prices = [200000, 45000, 150000, 30000, 15000]

products_data = list(zip(product_names, product_categories, stock_levels, sales_data, prices))

total_stock = list(map(lambda stock: sum(stock), stock_levels))

total_sales = list(map(lambda sales: reduce(lambda x, y: x + y, sales), sales_data))

low_stock_products = list(filter(lambda product: sum(product[2]) < 500, products_data))

def projected_revenue():
    for product, sales, price in zip(product_names, sales_data, prices):
        yield product, sum(sales) * price

total_revenue_by_category = reduce(
    lambda acc, product: {
        **acc,
        product[1]: acc.get(product[1], 0) + sum(product[3]) * product[4]
    },
    products_data,
    {}
)

def main():
    print("Product Details:")
    for product in products_data:
        print(product)

    print("\nTotal Stock:")
    for product, stock in zip(product_names, total_stock):
        print(f"{product}: {stock}")

    print("\nTop 3 Selling Products:")
    top_3_products = sorted(zip(product_names, total_sales), key=lambda x: x[1], reverse=True)[:3]
    for product, sales in top_3_products:
        print(f"{product}: {sales}")

    print("\nLow Stock Products:")
    for product in low_stock_products:
        print(product[0])

    print("\nProjected Revenue for Each Product:")
    for product, revenue in projected_revenue():
        print(f"{product}: {revenue}")

    print("\nRevenue Summary by Category:")
    for category, revenue in total_revenue_by_category.items():
        print(f"{category}: {revenue}")

main()
