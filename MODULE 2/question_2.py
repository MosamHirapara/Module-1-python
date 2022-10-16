# Write a Python function to get the largest number,smallest num and sum of all from a list.

#Problem



def max_and_min():
    myList = []
    numbers = int(input("How many numbers do you want: "))
    total = 0

    for i in range(numbers):
        element = int(input("Enter Elements: "))
        myList.append(element)
        total = sum(myList)
    

    print("Largest Number In List is:",max(myList))    
    print("Smallest Number In List is:",min(myList))
    print("Sum of all Numbers is:",total)
 
max_and_min()

