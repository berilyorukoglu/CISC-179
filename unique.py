inputFile = input("File to open: ")
textFile = open(inputFile)
uniqueWords = []
for line in textFile:
    words = line.split()
    for currentWord in words:
        currentWord = currentWord.strip('?,.!')     #Strip wierd characters from word
        if currentWord not in uniqueWords:          #is the word in the list
            uniqueWords.append(currentWord)         #if not, append to the list


uniqueWords.sort()
for currentWord in uniqueWords:
    print(currentWord)

textFile.close()

