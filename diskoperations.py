import os

currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)

print("Current path: ", currentDirectoryPath)
print("File names  in path: ", listOfFileNames)
for name in listOfFileNames:
    try:
        name.index('e')
        res = "Element found"
    except ValueError:
        res = "Element NOT found"
    print(res)

data = "myprogram.exe"
print(len(data))
print(data[(len(data)-1)//2:(len(data)+2)//2])

print(data[::-1])

s1 = ''
length = len(data) - 1
while length >= 0:
    s1 = s1 + data[length]
    length = length - 1
print(s1)






