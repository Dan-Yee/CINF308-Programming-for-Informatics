"""
Exericise 13.3: Modify the program from the previous exercise to print the 20 most frequently-used words in the book.
"""

from collections import defaultdict
import string
import heapq                                                                        # used to get the 20 most frequently used words

def exercise_13_3():
    wordCounts = defaultdict(lambda: 0)                                             # default dictionary that starts counting every element from 0
    
    file = open("great_gatsby_text.txt", "r")
    lines = file.readlines()
    file.close()
    
    bookStartIndex = lines.index("*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***\n") + 1
    bookEndIndex = lines.index("*** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***\n")
    lines = lines[bookStartIndex : bookEndIndex]
    
    for line in lines:
        line = line.lower()                                                         # convert everything to lowercase
        line = line.translate(str.maketrans('', '', string.punctuation))            # strip all punctuation out
        
        words = line.split()                                                        # break every line into words and remove all white space characters
        for word in words:
            wordCounts[word] = wordCounts["word"] + 1
    
    heap = list()
    for key, value in wordCounts.items():
        heap.append((-value, key))
    heapq.heapify(heap)
    
    print("The 20 most frequently used words are:\n")
    for i in range(20):
        value = heapq.heappop(heap)
        print(value[1], "with", value[0]*-1, "instances.")
    
exercise_13_3()