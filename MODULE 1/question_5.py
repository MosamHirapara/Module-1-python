# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

num = int(input("Enter Your Number: "))

sum = num % 2

if sum > 0:
    print("The Given Number is Odd")
else:
    print("The Given Number is Even" )    