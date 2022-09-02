#Write a Python func�on that takes a list of words and returns the length of the longest one.

mylist= ['PHP', 'Android','Python','C','c++']

list = []
for i in mylist:
    list.append((len(i)))
list.sort()
print(list)
print(list[-1:])