#Write a Python program to calculate surface volume and area of a cylinder.
pi = 22/7
height = float(input("Enter Height of Cylinder: "))
radius = float(input('Enter Radius of Cylinder: '))

volume = (pi)*(radius)*(radius)*(height)
surface_area = ( 2 * pi * radius * height ) + ( 2 * pi * radius * radius ) 

print("Volume of Cylinder is:",volume)
print("Surface area of Cylinder is:",surface_area)