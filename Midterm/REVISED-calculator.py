arithmeticOperations = tuple(["+", "-", "*", "/", "^2", "x^y"])
calculatorOperations = tuple(["HISTORY", "CLEARHISTORY", "CLEAR", "QUIT"])
history = list()
lastResult = None
operation = None

def displayOperations():
    print("Calculator Operations:\n")
    print("Arithmetic: ")
    for arithmeticOp in arithmeticOperations:
        print("\t", arithmeticOp)
    print()
    print("Other: ")
    for calculatorOp in calculatorOperations:
        print("\t", calculatorOp.title())
    print()

def getOperands():
    if operation == arithmeticOperations[4]:                                # special case for the squared operation
        if lastResult == None:
            num1 = int(input("Enter the first operand: "))
            return tuple(list(num1))
        else:
            return tuple(list(lastResult))
    if operation == None or operation in calculatorOperations:
        return
    if lastResult == None:                                                  # if the most recent calculation was None, ask for two operands
        num1 = int(input("Enter the first operand: "))
        num2 = int(input("Enter the second operand: "))
        return num1, num2
    else:                                                                   # otherwise, only ask for one
        num2 = int(input("Enter the second operand: "))
        return lastResult, num2

def printHistory():
    print("History:")
    for entry in history:
        print("\t", entry)

hasNextOperation = True
while(hasNextOperation):
    displayOperations()
    print()
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
        continue
    elif(operation == calculatorOperations[1]):                     # handles clearing history
        history.clear()
        print("History cleared!")
        continue
    elif(operation == calculatorOperations[2]):                     # handles clearing most recent result
        lastResult = None
        continue
    elif(operation == calculatorOperations[3]):                     # handles quitting program
        hasNextOperation = False
        continue

    # display the final result of the operation performed by the calculator
    if operation == arithmeticOperations[4]:                        # special handling of the square operator
        historyResult = str(operands[0]) + "^ 2 =" + str(lastResult)
        print(historyResult)
    elif operation == arithmeticOperations[5]:                      # special handling of the x^y operation
        historyResult = str(operands[0]) + "^" + str(operands[1]) + " = " + str(lastResult)
        print(historyResult)
    else:                                                           # all other operations
        historyResult = str(operands[0]) + " " + operation + " " + str(operands[1]) + " = " + str(lastResult)
        print(historyResult)
    # add the operation to history list
    history.append(historyResult)