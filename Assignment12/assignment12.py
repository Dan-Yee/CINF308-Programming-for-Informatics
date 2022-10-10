"""
Class to represent basic employee information for a small company
"""
class Employee:
    def __init__(self, first_name : str, last_name : str, phone_number : str, date_of_birth : str) -> None:
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.phone_number = phone_number.upper()
        self.date_of_birth = date_of_birth.upper()
    
    """
    Class function to return the employee's first and last name
    """
    def getName(self) -> str:
        return (self.first_name + " " + self.last_name).title()
    
    """
    Class function to display this specific employee's information
    (Only used for console display)
    """
    def displayInfo(self) -> None:
        print("Employee Information for:")
        print("\tName: " + self.getName())
        print("\tPhone Number: " + self.phone_number.title())
        print("\tDate of Birth: " + self.date_of_birth.title())
    
    """
    Class function to format all employee information into a String that can be written to a file
    (Only used for writing to a file (i.e., storing in a "database"))
    """
    def writeFileString(self) -> str:
        return self.getName() + " " + self.phone_number.title() + " " + self.date_of_birth.title()

####################################################################################################
userActions = ("LIST", "SEARCH", "UPDATE", "DELETE", "NEW", "QUIT")
local_storage = list()                   # list to store employee info that needs to be written to the file

"""
Function to update the "database" by overwriting the file that acts as the database
"""
def updateDatabase():
    dataFile = open("employee_info.txt", "w")
    
    for entry in local_storage:
        dataFile.write(entry.writeFileString() + "\n")
    dataFile.close()
"""
Function to handle listing all current employee information
"""
def listFunction():
    print("--------------------------------------------------< BEGIN LIST >--------------------------------------------------\n")
    for entry in local_storage:
        entry.displayInfo()
        print()
    print("--------------------------------------------------< END LIST >--------------------------------------------------")

"""
Function to handle searching for an existing employee record by name
"""
def searchFunction():
    searchName = input("Enter the employee's full name: ")
    searchName = searchName.upper()
    result = None
    
    for entry in local_storage:
        if searchName.title() == entry.getName():
            result = entry
            break
    
    if result == None:
        print("Employee named \"" + searchName.title() + "\"", "not found.")
    else:
        result.displayInfo()
        print()

"""
Function to handle updating a specific piece of information in an employee's record
"""
def updateFunction():
    # date of birth cannot be updated
    updateOptions = ("FIRSTNAME", "LASTNAME", "PHONE")
    
    searchName = input("Enter the employee's full name: ")
    searchName = searchName.upper()
    searchResult = None
    for entry in local_storage:
        if searchName.title() == entry.getName():
            searchResult = entry
            local_storage.remove(entry)
            break
    
    if searchResult == None:
        print("ERROR: Cannot find the employee to update.")
    else:
        infoToUpdate = input("Which piece of information did you want to update? \n\t\"FIRSTNAME\" \n\t\"LASTNAME\" \n\t\"PHONE\" \nYour Choice: ")
        infoToUpdate = infoToUpdate.upper()
        while infoToUpdate not in updateOptions:
            print("UPDATE ERROR: Field to update not recognized.")
            infoToUpdate = input("\nWhich piece of information did you want to update? \n\t\"FIRSTNAME\" \n\t\"LASTNAME\" \n\t\"PHONE\" \nYour Choice: ")
            infoToUpdate = infoToUpdate.upper()
        
        if infoToUpdate == updateOptions[0]:                                    # first name
            newInfo = input("Enter the employee's new first name: ")    
            searchResult.first_name = newInfo                               
        elif infoToUpdate == updateOptions[1]:                                  # last name
            newInfo = input("Enter the employee's new last name: ")
            searchResult.last_name = newInfo
        elif infoToUpdate == updateOptions[2]:                                  # phone number
            newInfo = input("Enter the employee's new phone number: ")
            searchResult.phone_number = newInfo
        local_storage.append(searchResult)
        updateDatabase()
        print("Employee information successfully updated")

"""
Function to delete an existing employee's information
"""
def deleteFunction():
    searchName = input("Enter the employee's full name: ")
    searchName = searchName.upper()
    searchResult = None
    for entry in local_storage:
        if searchName.title() == entry.getName():
            searchResult = entry
            local_storage.remove(entry)
            break
    
    if searchResult == None:
        print("ERROR: Cannot find the employee to delete.")
    else:
        updateDatabase()
        print("Employee successfully removed from database.")

"""
Function to handle creating a new "database" entry to store employee information
"""
def newFunction():
    print("Creating new employee...\n")
    first_name = input("Enter the employee's first name: ")
    last_name = input("Enter the employee's last name: ")
    phone_number = input("Enter the employee's phone number: ")
    date_of_birth = input("Enter the employee's date of birth (MM/DD/YYYY): ")
    
    newEmployee = Employee(first_name, last_name, phone_number, date_of_birth)
    local_storage.append(newEmployee)
    updateDatabase()
    print("New employee successfully created.")

# Main driver portion of the program
# attempt to read existing data in the file first
print()
try:
    dataFile = open("employee_info.txt", "r")
    print("Existing data found. Loading...\n")
    for entry in dataFile:
        info = entry.split()
        employee = Employee(info[0], info[1], info[2], info[3])
        local_storage.append(employee)
    dataFile.close()
except FileNotFoundError:
    print("No existing employee data found.\n")

# continually ask the user what action they want to do next
continueProgram = False
while not(continueProgram):
    action = input("Please select an action:\n\t\"LIST\" \n\t\"SEARCH\" \n\t\"UPDATE\" \n\t\"DELETE\" \n\t\"NEW\" \n\t\"QUIT\" \nYour Choice: ")
    action = action.upper()
    while action not in userActions:                                            # input validation
        print("\nERROR: Action not recognized. Please try again.")
        action = input("Please select an action:\n\t\"LIST\" \n\t\"SEARCH\" \n\t\"UPDATE\" \n\t\"DELETE\" \n\t\"NEW\" \n\t\"QUIT\" \nYour Choice: ")
        action = action.upper()
    
    print()
    if action == userActions[0]:                                                # LIST
        listFunction()
    elif action == userActions[1]:                                              # SEARCH
        searchFunction()
    elif action == userActions[2]:                                              # UPDATE
        updateFunction()
    elif action == userActions[3]:                                              # DELETE
        deleteFunction()
    elif action == userActions[4]:                                              # NEW
        newFunction()
    elif action == userActions[5]:                                              # QUIT
        continueProgram = True
        updateDatabase()
        print("Saving all data...\n")
    print()