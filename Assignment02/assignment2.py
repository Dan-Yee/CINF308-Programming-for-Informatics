# Single Filers Income Tax Calculator (based on 2022 Federal Income Tax brackets)
# Source for tax brackets: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets

continueProgram = True
while(continueProgram):
    taxableIncome = float(input("Please enter your taxable income: $"))

    taxOwed = 0
    taxBracket = 10
    if(taxableIncome < 0):
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
    
    print("Your taxable income was $", format(taxableIncome, ",.2f"), sep = "")
    print("Based on the 2022 Federal Income Tax brackets, you are in the ", taxBracket, "% tax bracket and owe $", format(taxOwed, ",.2f"), " in federal income taxes.", sep = "")

    loopProgram = input("\nWould you like to compute the 2022 Federal Income Tax for another amount? (y/n): ")
    while(not(loopProgram.lower() == "y" or loopProgram.lower() == "n")):
        print("Response not recognized: Please enter \"y\" or \"n\".")
        loopProgram = input("Would you like to compute the 2022 Federal Income Tax for another amount? (y/n): ")
    if(loopProgram.lower() == "n"):
        print("Have a good day!")
        continueProgram = False