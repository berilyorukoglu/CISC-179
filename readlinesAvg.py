with open("integers.txt", "r") as file:
    count = 0
    total = 0
    for readline in file:
        count += 1
        total += int(readline.strip())

    average = (total/count)
    print('{:.2f}'.format(average))

