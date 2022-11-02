#Write a Python program to map two lists into a dictionary

list1 = ['mosam','smit','vadil','bhumil']
list2 = [9.7,8.6,6.8,3.2]

dictionary = dict(zip(list1, list2))
print(dictionary)