# Write a Python function to calculate the factorial of a number (a non negativve integer)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter Your Number to compute factorial: "))
print(factorial(n))            