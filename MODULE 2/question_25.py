# Write a Python program to unzip a list of tuples into individual lists.

tupleList = [(1,2,3),(4,5,6),(7,8,9)]

myList = list(zip(*tupleList))
print(myList)