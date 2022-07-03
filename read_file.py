import csv
import os

f = open("Student_Data.csv", "r")

reader = csv.reader(f)

#    if f.mode=="r":
#        contents = f.read()
#        print(contents)
#    else:
#        print("File not open for read")

# students = []
# for row in reader:
#     try:
#        students.append(row)
#     except:
#        pass
#
#     #fl = f.readlines()
#     #for x in fl:
#     #    print(x)
#
# for item in students:
#     sname=item[0]
#     print(item)
#
# f.close()

print(os.getcwd())

print(os.environ)







