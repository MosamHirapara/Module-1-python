#Write a Python program to find the first appearance of the substring 'not' and 'poor' froma given string, if 'not' follows the 'poor', replace the whole'not'...'poor'substring with 'good'. Return the resul�ng string.

myStr= "This is not right code, this is poor Code"

n= myStr.find('not')
p= myStr.find('poor')

if p>n and n>0 and p>0:
    myStr=myStr.replace(myStr[n:(p+4)],'good')
    print(myStr)