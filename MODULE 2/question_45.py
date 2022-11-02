#Write a Python program to calculate the area of a trapezoid

height = float(input("Enter Height of Trapezoid: "))
base1 = float(input("Enter base1 of Trapezoid: "))
base2 = float(input("Enter base2 of Trapezoid: "))

area = ( ( base1 + base2 ) /2 ) * height

print(f"Area is : {area}")