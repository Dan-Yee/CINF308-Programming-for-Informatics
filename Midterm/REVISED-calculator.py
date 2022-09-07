from time import sleep

arithmeticOperations = tuple(["+", "-", "*", "/", "^2", "X^Y"])                         # all arithmetic operations
calculatorOperations = tuple(["HISTORY", "CLEAR HISTORY", "CLEAR", "QUIT"])             # all calculator operations
history = list()                                                                        # list for calculator history
lastResult = None
operation = None

"""
Function that displays all the available calculator and arithmetic operations that this program can handle
"""
def displayOperations():
    print("\n----------< Calculator Operations >----------")
    print("\tArithmetic: ")
    for arithmeticOp in arithmeticOperations:
        print("\t", arithmeticOp)
    print()
    print("----------< Other Operations >----------")
    for calculatorOp in calculatorOperations:
        print("\t", calculatorOp.title())
    print()

"""
Function that accepts input to be used as operands in arithmetic operations.
Function also handles special cases of when the result of a recent operation can be used (only asks for single input rather than two)
"""
def getOperands():
    if operation == arithmeticOperations[4]:                                # special case for the squared operation
        if lastResult == None:
            num1 = int(input("Enter the first operand: "))
            return (num1,)
        else:
            return (lastResult),
    if operation == None or operation in calculatorOperations:
        return
    if lastResult == None:                                                  # if the most recent calculation was None, ask for two operands
        num1 = int(input("Enter the first operand: "))
        num2 = int(input("Enter the second operand: "))
        return num1, num2
    else:                                                                   # otherwise, only ask for one
        num2 = int(input("Enter the second operand: "))
        return lastResult, num2

"""
Function that prints the history of calculator operations -- only stores arithmetic operations
"""
def printHistory():
    print("-----< History: >-----")
    if len(history) is 0:
        print("\tNo History")
    else:
        for entry in history:
            print("\t", entry)

"""
Program continues to accept input (requests for arithmetic or calculator operations) until the user decides to quit
"""
hasNextOperation = True
while(hasNextOperation):
    displayOperations()
    print()
    if lastResult is not None:
        print("Last Result:", lastResult)
    operation = input("Select an operation: ")
    operation = operation.upper()
    while operation not in arithmeticOperations and operation not in calculatorOperations:
        print("\nOperation not recognized. Please try again.")
        operation = input("Select an operation: ")
        operation = operation.upper()

    operands = getOperands()
    if(operation == arithmeticOperations[0]):                       # handles addition
        lastResult = operands[0] + operands[1]
    elif(operation == arithmeticOperations[1]):                     # handles subtraction
        lastResult = operands[0] - operands[1]
    elif(operation == arithmeticOperations[2]):                     # handles multiplication
        lastResult = operands[0] * operands[1]
    elif(operation == arithmeticOperations[3]):                     # handles division
        lastResult = operands[0] / operands[1]
    elif(operation == arithmeticOperations[4]):                     # handles square operation
        lastResult = operands[0] ** 2
    elif(operation == arithmeticOperations[5]):                     # handles x^y operation
        lastResult = operands[0] ** operands[1]
    elif(operation == calculatorOperations[0]):                     # handles viewing history
        printHistory()
        sleep(5)                                                    # delay program to allow user to read history
        continue
    elif(operation == calculatorOperations[1]):                     # handles clearing history
        history.clear()
        print("History Cleared!")
        continue
    elif(operation == calculatorOperations[2]):                     # handles clearing most recent result
        lastResult = None
        print("Calculator Cleared!")
        continue
    elif(operation == calculatorOperations[3]):                     # handles quitting program
        hasNextOperation = False
        continue

    # display the final result of the operation performed by the calculator
    if operation == arithmeticOperations[4]:                        # special handling of the square operator
        historyResult = str(operands[0]) + " ^ 2 = " + str(lastResult)
        print("Result of", historyResult)
    elif operation == arithmeticOperations[5]:                      # special handling of the x^y operation
        historyResult = str(operands[0]) + " ^ " + str(operands[1]) + " = " + str(lastResult)
        print("Result of", historyResult)
    else:                                                           # all other operations
        historyResult = str(operands[0]) + " " + operation + " " + str(operands[1]) + " = " + str(lastResult)
        print("Result of", historyResult)
    # add the operation to history list
    history.append(historyResult)
    sleep(3)                                                        # delay the program to give the user time to read results