
prices={
    "rice":75,
    "oil":185,
    "sugar":120,
    "milk":95,
    "egg":12,
    "flour":65,
    "salt":40,
    "lentil":130,
    "potato":45,
    "onion":80,
    "tea":250,
    "coffee":450,
    "biscuit":50,
    "soap":70,
    "shampoo":180
}

print("========== AVAILABLE PRODUCTS ==========")
for item, price in prices.items():
    print(f"{item:<12} Tk {price:.2f}")

order = {}

entries = int(input("\nHow many order entries? "))

for i in range(entries):
    item=input(f"Enter product {i+1}:").strip().lower()

    if item not in prices:
        print(f"{item} is not available.")
        continue
    try:
        quantity=int(input("Enter quantity:"))
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        continue

    if quantity<=0:
        print("Quantity must be positive.")
        continue

    order[item] = order.get(item, 0) + quantity

print("\n========== FINAL COMBINED ORDER ==========")
print(order)

bill={}
subtotal=0

for item, quantity in order.items():
    unit_price=prices[item]
    total=quantity*unit_price

    bill[item]={
        "quantity":quantity,
        "unit_price":unit_price,
        "total":total
    }

    subtotal+=total

if subtotal>=1000:
    discount=subtotal*0.05
else:
    discount=0

vat=(subtotal-discount)*0.02
final_amount=subtotal-discount+vat

print("\n================ GROCERY SHOP BILL ================")
print(f"{'Item':<12}{'Quantity':>10}{'Unit Price':>14}{'Total':>12}")
print("-" * 50)

for item, details in bill.items():
    print(
        f"{item:<12}"
        f"{details['quantity']:>10}"
        f"{details['unit_price']:>14.2f}"
        f"{details['total']:>12.2f}"
    )

print("-" * 50)
print(f"{'Subtotal:':<25} Tk {subtotal:.2f}")
print(f"{'Discount (5%):':<25} Tk {discount:.2f}")
print(f"{'VAT (2%):':<25} Tk {vat:.2f}")
print("-" * 50)
print(f"{'Final amount:':<25} Tk {final_amount:.2f}")
print("=" * 52)