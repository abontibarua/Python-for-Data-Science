words=["model","data","python","data","model","analysis","data"]
frequency={}
for word in words:
    frequency[word]=frequency.get(word,0)+1

repeated=[word for word,count in frequency.items() if count>1]
print(f"Frequency:{frequency}")
print(f"Repeated words:{repeated}")