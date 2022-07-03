f = open("words", "r")
text = f.read()
textlist = text.split()
for word in textlist:
    if len(word) ==4:
        print(word)