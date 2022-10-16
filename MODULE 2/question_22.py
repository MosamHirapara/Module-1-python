# Write a Python program to replace last value of tuples in a list

list = [(20,30,40), (40,50,60), (70,80,90)]
print([z[:-1] + (100,) for z in list])