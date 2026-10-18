stock={"pen":12,"book":3,"bag":2,"ruler":9,"calculator":1}
total_units=sum(stock.values())
low_stock={product: quantity for product, quantity in stock.items() if quantity < 5}
print(f"Total units:{total_units}")
print(f"Low stock:{low_stock}")