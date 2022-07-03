import random

"""
f = open("test.txt", 'w')

f.write("This is the first line\nThis is the second line\n")

f.close()
"""

count = 0
f = open("integers.txt", 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')

f.close()
