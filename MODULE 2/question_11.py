# Write a Python program to find the second smallest number in a list
num = int(input("How Many Numbers Do you Want: "))
myList = []


for i in range(num):
    x = int(input("Enter Your Number List: "))
    myList.append(x)

lenghth = len(myList)
myList.sort()

print("Second Smallest Element is:",myList[1])