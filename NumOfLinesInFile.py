with open("myfile.txt", "r") as file:
    count = 0
    for readline in file:
        count += 1

print("Number of lines in file: ", count)