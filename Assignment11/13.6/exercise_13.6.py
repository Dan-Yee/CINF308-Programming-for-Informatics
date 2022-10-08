"""
Exercise 13.6: Write a program that uses set substraction to find words in the book that are not in the word list.
"""
import string

def exercise_13_6():
    wordSet = set()
    bookWords = set()
    
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
        
        bookWords.update(line.split())                                              # add all the words from the current line to the set
        
    words_not_in_set = wordSet - bookWords                                          # use set subtraction to subtract remove all words of the book from the set of words
    
    print(words_not_in_set)
    print("\nAbove is the set of words that were not found in the book.")
    print(len(words_not_in_set), "of the", len(wordSet), "words in the word list were not present in the book.")
            

exercise_13_6()