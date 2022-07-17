ignore_list = ["and", "or", "is", "this", "that", "a", "an", 'are', "for", "of", "the", "to",
               "with", "you", "your", "our", "can", 'it', 'in', 'has', 'have', 'all', 'also', 'will',  'we', 'us', 'them',  'they']
f = open("freq_words", 'r')

# Input the text, convert its words to uppercase, and
# add the words to a list
words = []
word_count = 0
for line in f:
    for word in line.split():
        check = word.strip("!?,;)(.").lower()
        word_count += 1
        if check not in ignore_list:
            words.append(check)
        else:
            print("ignored word", check)

# Obtain the set of unique words and their
# frequencies, saving these associations in
# a dictionary

theDictionary = {}
for word in words:
    freq = theDictionary.get(word, None)
    if freq is None:
        # word entered for the first time
        theDictionary[word] = 1
    else:
        # word already seen, increment its number
        theDictionary[word] = freq + 1

# Find the mode by obtaining the maximum value
# in the dictionary and determining its key

theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The most frequently used word is :", key, " and occurs ", theMaximum, " times")
        break

# print("The length of the text is : ", len(words))
# print("The length of the dictionary is : ", len(theDictionary))

print(theDictionary)
print("The total word count is :", word_count)

sorted_dict = {}
sorted_keys = sorted(theDictionary, key=theDictionary.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = theDictionary[w]

print(sorted_dict)

for word, value in sorted_dict.items():
    if value > 5:
        density = round((100*value)/word_count, 2)
        print(word, value, density)


