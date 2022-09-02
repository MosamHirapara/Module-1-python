# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def swap():
    myStr1= input("Enter Your First Word: ")
    myStr2= input("Enter Your Second Word: ")

    x = myStr1[0:2]  

    myStr1 = myStr1.replace(myStr1[0:2],myStr2[0:2]) 

    myStr2 = myStr2.replace(myStr2[0:2], x)

    print(myStr1+" "+myStr2)

swap()