# Write a Python program to get the Fibonacci series of given range.

numbers = int(input("Enter Your Number Range: "))

n1 = 0
n2 = 1
sum = 0

if numbers<= 0 :
    print("Enter Postive Integer")

elif numbers == 1 :
    print(f"Fibonacci sequence upto {numbers}")
    print(n1)

else:
    print("Fibonacci sequence: ")
    for i in range(numbers):
        print(sum, end=" ")
        n1 = n2     
        n2 = sum
        sum = n1+n2