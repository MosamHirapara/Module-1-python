#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. Ifthe string length islessthan 2,return instead of the empty string

def string(myStr):
    length = len(myStr)
    if length> 2:
        return myStr[0:2] + myStr[-2:]
    else:
        return'' 

print(string(input("Enter Your Favourite Word: ")))