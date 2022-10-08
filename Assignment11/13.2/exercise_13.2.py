"""
Exercise 13.2: 
- Download your favorite out-of-copyright book in plain text format.
- Modify your program from the previous exercise to read the book you downloaded,
skip over the header information at the beginning of the file, and process the rest of the words as before
- Modify your program to count the total number of words in the book and the number of times each word is used
"""
from collections import defaultdict
import string

def exercise_13_2():
    wordCounts = defaultdict(lambda: 0)                                             # default dictionary that starts counting every element from 0
    totalWords = 0
    
    file = open("great_gatsby_text.txt", "r")
    #file = open("history_of_scientific_ideas.txt", "r")
    lines = file.readlines()
    file.close()
    
    """
    For "History of Scientific Ideas", uncomment the below two lines and comment out the originally uncommented two
    Also uncomment the open() statement above for the text you want to test
    """
    #bookStartIndex = lines.index("IDEAS ***\n") + 1
    #bookEndIndex = lines.index("*** END OF THE PROJECT GUTENBERG EBOOK HISTORY OF SCIENTIFIC\n")
    
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
        totalWords += len(words)
        for word in words:
            wordCounts[word] = wordCounts["word"] + 1
    
    
    # Display final information
    for key, value in wordCounts.items():
        print(key, "was used", value, "times.")
    print()
    print("There were a total of", totalWords, "words in this book.")
    print("Of those", totalWords, "words,", len(wordCounts), "were unique.")
    
exercise_13_2()