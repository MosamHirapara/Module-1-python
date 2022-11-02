# Write a Python script to concatenate following dictionaries to create a new one

dictionary1 = {"Mosam":25, "Vadil":29}

dictionary2 = {"Smit":8, "Bhumil":16}

dictionary3 = {"Nirav": 39, "Yash":2}

dictionary4 = {}

for i in (dictionary1,dictionary2,dictionary3):
    dictionary4.update(i)

print(dictionary4)    