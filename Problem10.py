
sales = [
    {"product":"Pen", "quantity":3, "price":15},
    {"product":"Book", "quantity":2, "price":120},
    {"product":"Pen", "quantity":5, "price":15},
    {"product":"Bag", "quantity":1, "price":850},
    {"product":"Book", "quantity":-1, "price":120},
    {"product":"Ruler", "quantity":4, "price":20}
]

product_revenue={}
total_revenue=0
high_revenue_transactions=[]
invalid_records=0

for sale in sales:
    quantity=sale["quantity"]
    price=sale["price"]
    product=sale["product"]

    if quantity<=0 or price<0:
        invalid_records+=1
        continue

    revenue=quantity*price

    if product in product_revenue:
        product_revenue[product]+=revenue
    else:
        product_revenue[product]=revenue

    total_revenue+=revenue

    if revenue>=200:
        high_revenue_transactions.append({
            "product":product,
            "quantity":quantity,
            "price":price,
            "revenue":revenue
        })

highest_product=max(product_revenue, key=product_revenue.get)
highest_revenue=product_revenue[highest_product]

print("Revenue by Product:")
for product, revenue in product_revenue.items():
    print(f"{product}:Tk {revenue}")

print("\nTotal Revenue:Tk", total_revenue)

print("\nProduct with Highest Revenue:")
print(f"{highest_product}:Tk {highest_revenue}")

print("\nTransactions with Revenue>=Tk 200:")
for transaction in high_revenue_transactions:
    print(transaction)

print("\nNumber of Invalid Records:", invalid_records)