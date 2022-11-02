# Write a Python script to merge two Python dictionaries

dict1 = {"name":"Mosam","sem":5}
dict2 = {"Name":"Smit","Sem":6}
dict = {}
for x in(dict1 , dict2):
    dict.update(x)

print(dict)    



#another method

dict3 = {"game":"Kabbadi","gem":51}
dict4 = {"Game":"Khokho","Gem":62}

d = dict3.copy()
d.update(dict4)

print(d)

