namesList = list()
eyeHairColor = list()
stateCities = dict()

def displayAllData():
    print("You Entered:\n")
    for name, eyeHair in zip(namesList, eyeHairColor):
        print("Name:", name)
        print("\tEye Color:", eyeHair[0])
        print("\tHair Color:", eyeHair[1])

    for state, citySet in stateCities.items():
        print("State:", state)
        print("\tCities entered:", citySet)

hasMoreData = True
while(hasMoreData):
    # ask to enter a data entries name
    name = input("Please enter a name: ")
    namesList.append(name.title())

    # ask to enter a data entries eye and hair color
    print("Please enter ", name.title(), "'s eye color: ", end = "", sep = "")
    eyeColor = input("")
    print("Please enter ", name.title(), "'s hair color: ", end = "", sep = "")
    hairColor = input("")
    eyeHairColor.append(tuple([eyeColor, hairColor]))

    # ask to enter data entries state and city
    print("Please enter ", name.title(), "'s home state: ", end = "", sep = "")
    state = input("")
    print("Please enter ", name.title(), "'s home city: ", end = "", sep = "")
    city = input("")

    # if the state was already entered previously, append the city to the set associated with the state
    # otherwise, create a new set for the new state entered
    if(state.title() in stateCities.keys()):
        stateCities[state.title()].add(city.title())
    else:
        stateCities[state.title()] = set()
        stateCities[state.title()].add(city.title())

    # check if the user wants to input more data
    userInput = input("\n\nWould you like to enter more user data? (yes/no): ")
    userInput = userInput.lower()
    while(not(userInput == "yes" or userInput == "no")):
        print("Response not recognized. Please try again.")
        userInput = input("Would you like to enter more user data? (yes/no): ")
        userInput = userInput.lower()
    if(userInput == "no"):
        print("Thank you and have a nice day!")
        displayAllData()
        hasMoreData = False