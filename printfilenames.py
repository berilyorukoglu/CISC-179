import os

currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)

print("Current path: ", currentDirectoryPath)
print("File names  in path: ", listOfFileNames)

