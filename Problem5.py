from collections import Counter

delivery_1={"pen":12,"book":5,"bag":2}
delivery_2={"book":4,"ruler":10,"pen":3}

combined_delivery=dict(Counter(delivery_1)+Counter(delivery_2))

grand_total=sum(combined_delivery.values())

print(f"Combined delivery:{combined_delivery}")
print(f"Grand total:{grand_total}")