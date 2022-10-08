"""
Exercise 13.1: Write a program that reads a file, breaks each line into words, 
stripes whitespace and punctuation from the words and convert them to lowercase
"""
import string

def exercise_13_1():
    result = list()
    
    file = open("exercise_13.1.txt", "r")
    
    for line in file:
        line = line.lower()                                                         # convert everything to lowercase
        line = line.translate(str.maketrans('', '', string.punctuation))            # strip all punctuation out
        result.extend(line.split())                                                 # strips all white space characters
    
    print("Reading from \"exercise_13.1.txt\"")   
    print("Exercise 13.1 Results:", result)

exercise_13_1()