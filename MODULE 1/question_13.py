#Write a Python program to count the occurrences of each word in a given sentence
# myStr = "lion is king of jungle, but fox is not king of jungle, therefore king of jungle is lion"
# d1 = dict()
# for line in myStr:
#     words = line.split()
#     print(words)

#     for word in words:
#         if word in d1:
#             d1[word] = d1[word] + 1
#         else:
#             d1[word] = 1
# print(d1)                



# "Hi, this is python and this is VS code"

myStr = "This is Python and This is VScode"

count = dict()
word = myStr.split() 

print(word)

for i in word:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1    
print(count)        