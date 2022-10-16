#Write a Python program to get unique values from a list

myList = [30,20,20,10,16,78,76,64,78,30,32,16,98,76]
print(f"Original List: {myList}")

mySet = set(myList)

myNewList = list(mySet)
myNewList.sort()
print(f"List Of Unique Numbers: {myNewList}")