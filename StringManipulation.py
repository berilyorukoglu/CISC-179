name = "orhan yorukoglu"
new_Name = ""

i = 0
for i in range(0, len(name)):

    if (i % 2) == 0:
        character = name[i].upper()
    else:
        character = name[i]
    new_Name = new_Name + character
    i += 1

print(new_Name)

name = list(name)
print(name)

if name.__contains__("Q"):
    print("The name contains o")
else:
    print("The name does not contain o")

str1 = ""

# return string
name = str1.join(name)



print(name)
q = name.split("o")
print(q)

