stock={"pen":10, "book":5, "bag":2}

transactions=[
    {"type":"receive", "item":"pen", "quantity":4},
    {"type":"sell", "item":"book", "quantity":3},
    {"type":"sell", "item":"bag", "quantity":5},
    {"type":"receive", "item":"ruler", "quantity":6},
    {"type":"sell", "item":"pen", "quantity":8}
]

accepted=0
rejected=0

for transaction in transactions:
    item=transaction["item"]
    quantity=transaction["quantity"]

    if transaction["type"]=="receive":
        stock[item]=stock.get(item, 0)+quantity
        accepted+=1

    elif transaction["type"]=="sell":
        if stock.get(item, 0)>=quantity:
            stock[item]-=quantity
            accepted+=1
        else:
            print(f"Rejected sale: Not enough {item} in stock.")
            rejected+=1

print("\nFinal stock:", stock)
print("Accepted transactions:", accepted)
print("Rejected transactions:", rejected)