# Write a Python program to find the highest 3 values in a dictionary
from collections import Counter

myDict = {"A": 37,'B': 45, 'C': 28,'D' : 97,'E' : 123, 'F' : 20 }

k = Counter(myDict)
high = k.most_common(3)

print("Initial Dictionary: ")
print(myDict, '\n')

print(high)

print("Keys : Values")

for i in high:
    print(i[0],':',i[1])