# Write a Python function to check whether a number is in a given range

def check_range(n):
    if n in range (0,100):
        return("Yes it is in Range!!")
    else:
        return("Oops Not in Range!!")


n = int(input("Enter Your Number: "))        
print(check_range(n))