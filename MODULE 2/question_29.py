#Write a Python script to check if a given key already exists in a dictionary

dict1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

def is_key_present(x):
    if x in dict1:
        print("Key is Present In the Dictionary")
    if x not in dict1:
        print("Key is not Present In the Dictionary")

is_key_present(2)        
is_key_present(9)        