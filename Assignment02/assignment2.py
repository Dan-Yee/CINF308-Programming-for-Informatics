# Single Filers Income Tax Calculator (based on 2022 Federal Income Tax brackets)
# Source for tax brackets: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets

"""
This program asks the user to enter their taxable income and tells them the total federal income tax they owe, as well as which tax bracket they are in, based on the 2022 Federal Income Tax brackets.
The program also asks the user if they would like to compute the income tax owed on a different value of taxable income and allows them to keep doing so until they choose to quit.
"""
continueProgram = True                                                  # boolean flag to see if the program should be repeated
while(continueProgram):
    taxableIncome = float(input("Please enter your taxable income: $"))

    taxOwed = 0                                                         # smallest amount of tax owed is 0                              
    taxBracket = 10                                                     # lowest tax bracket is 10%
    if(taxableIncome < 0):                                              # determine which tax bracket the taxable income entered falls under
        print("Error: Taxable income cannot be negative")
        continue
    elif(taxableIncome >= 0 and taxableIncome <= 10275):
        taxOwed = taxableIncome * 0.1
    elif(taxableIncome >= 10276 and taxableIncome <= 41775):
        taxOwed = 1027.5 + ((taxableIncome - 10275) * 0.12)
        taxBracket = 12
    elif(taxableIncome >= 41776 and taxableIncome <= 89075):
        taxOwed = 4807.5 + ((taxableIncome - 41775) * 0.22)
        taxBracket = 22
    elif(taxableIncome >= 89076 and taxableIncome <= 170050):
        taxOwed = 15213.5 + ((taxableIncome - 89075) * 0.24)
        taxBracket = 24
    elif(taxableIncome >= 170051 and taxableIncome <= 215950):
        taxOwed = 34647.5 + ((taxableIncome - 170050) * 0.32)
        taxBracket = 32
    elif(taxableIncome >= 215951 and taxableIncome <= 539900):
        taxOwed = 49335.5 + ((taxableIncome - 215950) * 0.35)
        taxBracket = 35
    else:
        taxOwed = 162718 + ((taxableIncome - 539900) * 0.37)
        taxBracket = 37
    
    # display final results
    print("Your taxable income was $", format(taxableIncome, ",.2f"), sep = "")
    print("Based on the 2022 Federal Income Tax brackets, you are in the ", taxBracket, "% tax bracket and owe $", format(taxOwed, ",.2f"), " in federal income taxes.", sep = "")

    # check if the user wants to compute tax owed on a different value of taxable income
    loopProgram = input("\nWould you like to compute the 2022 Federal Income Tax for another amount? (y/n): ")
    while(not(loopProgram.lower() == "y" or loopProgram.lower() == "n")):
        print("Response not recognized: Please enter \"y\" or \"n\".")
        loopProgram = input("Would you like to compute the 2022 Federal Income Tax for another amount? (y/n): ")
    if(loopProgram.lower() == "n"):
        print("Have a good day!")
        continueProgram = False