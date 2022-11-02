#Write a Python program to print all unique values in a dictionary.

myList = [{"name":"movies"}, 
          {"name":"sports"}, 
          {'name':'music'},
          {"genre":"music"},
          {'genere':'music'},
          {'genre':'movies'},
          {'genre':'sports'},
          {'genre':'news'}, 
          {'genre':'sports'}]

set = set()
for x in myList:
    for y in x.values():
        set.add(y)

print(set)                  