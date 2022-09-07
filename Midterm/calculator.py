hasNextOperation = True
while(hasNextOperation):
    print("Select an operation: ")
    print("\tAddition (+)")
    print("\tSubtraction (-)")
    print("\tMultiplication (*)")
    print("\tDivision (/)")
    print("\tQuit (q)")

    operation = input("Select an operation: ")
    result = None
    if(operation == "+"):
        num1 = int(input("Enter the first operand: "))
        num2 = int(input("Enter the second operand: "))
        result = num1 + num2
    elif(operation == "-"):
        num1 = int(input("Enter the first operand: "))
        num2 = int(input("Enter the second operand: "))
        result = num1 - num2
    elif(operation == "*"):
        num1 = int(input("Enter the first operand: "))
        num2 = int(input("Enter the second operand: "))
        result = num1 * num2
    elif(operation == "/"):
        num1 = int(input("Enter the first operand: "))
        num2 = int(input("Enter the second operand: "))
        result = num1 / num2
    elif(operation == "q"):
        hasNextOperation = False
        continue
    else:
        print("Operation not recognized! Please try again.\n")
        continue
    
    print(num1, operation, num2, "=", result)
    print("\n")