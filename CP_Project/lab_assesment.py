
product_name=['laptop','tablet','smartphone','monitor','keyboard']
product_cat=['electronics','electronics','electronics','peripherrals','peripherrals']
stock_level=[[300,250,200],[500,450,400],[700,650,600],[400,350,300],[1000,950,900]]
sales_data=[[50,60,70,80,90,100],[30,35,40,45,50,55],[100,110,120,130,140,150],[20,25,30,35,40,45],[150,160,170,180,190,200]]
prices=[200000,45000,150000,30000,15000]

zip_list=list(zip(product_name,product_cat,stock_level,sales_data,prices))
# print(zip_list)
stock_avalable=list(map(lambda ziplist: sum(ziplist[2]),zip_list ))
# print(stock_avalable)
# top_sales=list(sales_data.)

# low_stock=list(filter(lambda ))
# # def generator()

#use filter to identify products with low stock
low_stock=list(filter(lambda ziplist: ziplist[2][0]<400,zip_list))

# print(low_stock)

def main():
    for i in range(len(product_name)):
        print(zip_list[i])

    for i in range(len(product_name)):
        
        print(f'{product_name[i] } : {stock_avalable[i]}')

    for i in range(len(low_stock)):
        print(f'{low_stock[i]}')
main()


