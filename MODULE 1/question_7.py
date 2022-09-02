# Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.

def threesum():

    x = int(input("Enter Your X Here: "))
    y = int(input("Enter Your Y Here: "))
    z = int(input("Enter Your Z Here: "))

    if x==y or y==z or z==x:
        sum = 0
    else:
        sum = x+y+z 
    print (sum)     


threesum()
