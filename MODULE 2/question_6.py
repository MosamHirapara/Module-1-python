# Write a Python function that takes two lists and returns true if they have at least one common member.

def common_data(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return(result)

print(common_data([1,2,3,4,5], [1,6,7,8,9,10]))
print(common_data([24,25,27,89,90], [1,2,3,4,5]))
