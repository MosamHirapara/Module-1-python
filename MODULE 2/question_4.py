# Write a Python program to remove duplicates from a list.

myList = [1,2,3,4,1,79,64,56,79,72,65]
myList = set(myList)
myList = list(myList)
myList.sort()
print(myList)



# 2nd method
myList2 = [1,2,3,4,1,69,54,46,69,62,85]

duplicate = set()
unique = []

for i in myList2:
    unique.append(i)
    duplicate.add(i)

print(duplicate)