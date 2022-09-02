# Write a python program to sum of the first n positive integers


num = int(input("Enter The Number: "))
sum= 0

  

if num == 0:
    print("The sum = 0")
elif num<0:
    print("Please Enter Postive Integer")
else:
    for i in range(1,num+1):
        sum+=i
    print(sum) 
             
 

    