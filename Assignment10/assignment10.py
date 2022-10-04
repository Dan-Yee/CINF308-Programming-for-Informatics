userActions = ("ADD", "SEARCH", "QUIT")
userElements = list()

"""
Function to sort the list, userElements, using the Insertion Sort algorithm
"""
def insertionSort():
    for i in range(1, len(userElements)):
        key = userElements[i]
        j = i - 1
        
        while j >= 0 and key < userElements[j]:
                userElements[j + 1] = userElements[j]
                j -= 1
        userElements[j + 1] = key

"""
Function to search for an element in userElements using the Binary Search algorithm
"""
def binarySearch(element):
    low = 0
    high = len(userElements) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        if userElements[mid] < element:
            low = mid + 1
        elif userElements[mid] > element:
            high = mid - 1
        else:
            return mid
    return -1

"""
Function to append numOfElement user inputs of numbers to a list
"""
def addElements(numOfElements):
    for i in range(numOfElements):
        value = int(input("Enter a value: "))
        userElements.append(value)
    insertionSort()
    print("The list of elements right now is", userElements)

# get the initial inputs since we can't really perform actions on an empty list
numOfElements = int(input("How many elements do you want to enter initially? "))
while numOfElements < 1:
    print("Value must be at least 1.")
    numOfElements = int(input("How many elements do you want to enter initially? "))
addElements(numOfElements)

# continue to ask the user what they want to do next
# they can ADD more elements to the list, SEARCH for an element or QUIT the program
print()
continueProgram = False
while not(continueProgram):
    action = input("What would you like to do now? (ADD, SEARCH or QUIT): ")
    action = action.upper()
    while action not in userActions:
        print("Action not recognized. Please try again.")
        action = input("What would you like to do now? (ADD, SEARCH or QUIT): ")
        action = action.upper()
    
    if action == userActions[0]:                                                               # "ADD"
        numOfElements = int(input("How many elements do you want to add? "))
        while numOfElements < 1:
            print("Value must be at least 1.")
            numOfElements = int(input("How many elements do you want to add? "))
        addElements(numOfElements)
    elif action == userActions[1]:                                                             # "SEARCH"
        element = int(input("What value do you want to search for? "))
        searchReturn = binarySearch(element)
        
        if searchReturn == -1:
            print("Element", element, "was not found in the list of elements.")
        else:
            print("Element", element, "was found at index", searchReturn, "in the list.")
    elif action == userActions[2]:                                                             # "QUIT"
        continueProgram = True
        print("Have a good day!")
    print()