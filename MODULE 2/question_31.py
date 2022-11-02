#Write a Python program to check multiple keys exists in a dictionary

classRoom = {
    'name': "Mosam",
    'Sem': 5,
    'Enrollment': 12
}

print(classRoom.keys() >= {'name', 'Sem'})
print(classRoom.keys() >= {'Sem', 'Sem'})
print(classRoom.keys() >= {'Sem', 'Mosam'})
print(classRoom.keys() >= {'name', 'Enrollment'})