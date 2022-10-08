"""
Exercise 13.4: Modify the previous program to read a word list and then print all the words in the book that are not in the word list. 
"""
from collections import defaultdict
import string

def exercise_13_4():
    wordCounts = defaultdict(lambda: 0)                                             # default dictionary that starts counting every element from 0
    wordSet = set()
    
    file = open("words.txt", "r")
    for word in file:
        wordSet.add(word.strip())
    file.close()
    
    file = open("great_gatsby_text.txt", "r")
    lines = file.readlines()
    file.close()
    
    bookStartIndex = lines.index("*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***\n") + 1
    bookEndIndex = lines.index("*** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***\n")
    lines = lines[bookStartIndex : bookEndIndex]
    
    for line in lines:
        line = line.lower()                                                         # convert everything to lowercase
        line = line.translate(str.maketrans('', '', string.punctuation))            # strip all punctuation out
        
        # replace the special looking characters that are a part of Windows
        line = line.replace("—", " ")
        line = line.replace("“", " ")
        line = line.replace("”", " ")
        line = line.replace("‘", " ")
        line = line.replace("’", " ")
        
        words = line.split()                                                        # break every line into words and remove all white space characters
        for word in words:
            wordCounts[word] = wordCounts["word"] + 1
    
    count = 0
    for key in wordCounts.keys():
        if key not in wordSet:
            print(key, "is not in the word list")
            count += 1
    print("\nIn total,", count, "words from the", len(wordSet), "words in the word list were not present in the book.")

exercise_13_4()