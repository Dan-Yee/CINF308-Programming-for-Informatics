"""
Exercise 13.5: Write a function "choose_from_hist" that takes a histogram and returns a random value from the histogram.
The value returned must be chosen with probability in proportion to frequency.
"""
import random

def choose_from_hist(histogram):
    elements = list()
    
    # convert the histogram to a list of elements by frequency
    for key, value in histogram.items():
        for i in range(value):
            elements.append(key)
    
    # return a random element, respecting probabilty
    return random.choice(elements)

test_histogram = {
    "a" : 25,               # expect "a" to be returned 50% of the time
    "b" : 15,               # expect "b" to be returned 30% of the time
    "c" : 10,               # expect "c" to be returned 20% of the time
}

print(type(test_histogram))
aCount = 0
bCount = 0
cCount = 0
for i in range(100):
    returned = choose_from_hist(test_histogram)
    if returned == "a":
        aCount += 1
    elif returned == "b":
        bCount += 1
    elif returned == "c":
        cCount += 1

print("The histogram used for testing was:", test_histogram)
print("The choose_from_hist function was executed 100 times. Of those 100 executions:")
print("\t\"a\" was returned", aCount, "times or about", (aCount / 100) * 100, "% of the time.")
print("\t\"b\" was returned", bCount, "times or about", (bCount / 100) * 100, "% of the time.")
print("\t\"c\" was returned", cCount, "times or about", (cCount / 100) * 100, "% of the time.")