#Write a Python program to add 'ing' at the end of a given string (lengthshould be at least 3). If the given string already ends with 'ing' then add 'ly'insteadif the string length of the given string is less than 3, leave itunchanged

myStr= input('Enter Your String: \n')
length = len(myStr)

if length > 2:
    if myStr[-3:] == "ing":
        myStr += 'ly'
    else:
        myStr += 'ing'

print(myStr)            