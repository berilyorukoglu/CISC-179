filename = input("Enter file name to open: ")
try:
    open(filename, 'r')
except:
    print("file does not exist")

