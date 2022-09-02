# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def sum():
    x = int(input("Enter The Value of X: "))
    y = int(input("Enter The Value of Y: "))

    if (x==y or (x-y)==5 or (x+y)== 5):
        print(True)
    else:
        print(False)    

sum()        