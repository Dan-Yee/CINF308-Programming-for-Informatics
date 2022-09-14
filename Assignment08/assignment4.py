# This program simulates a items available in a store and the ability to add/remove items from the shelf to add/remove them from the users cart
availableItems = ["MILK", "EGGS", "BREAD", "WATER", "COFFEE", "POTATOES", "LETTUCE", "PASTA", "RICE", "BEANS"]
cart = list()

"""
Function to display items either available on the shelf (availableItems) or in the users cart (cart)
"""
def displayItems(items):
    for item in items:
        print(item.title(), " ", end = "")
    print("\n")

"""
Function to print the available actions for the user to select from
"""
def printActions():
    print("What would you like to do?")
    print("\t- Add Item to Shopping Cart (Enter \"Add\")")
    print("\t- Remove Item from Shopping Cart (Enter \"Remove\")")
    print("\t- Quit and Start Over (Enter \"Quit\")")
    print("\t- Leave Store (Enter \"Leave\")")

print("Welcome to PyMarket!")
displayItems(availableItems)

isAddingItems = True
while(isAddingItems):
    printActions()
    action = input("\nSelect an Action: ")
    action = action.lower()
    while(not(action == "add" or action == "remove" or action == "quit" or action == "leave")):
        print("\nERROR: Action not recognized. Please try again.\n")
        printActions()
        action = input("Select an Action: ")
        action = action.lower()
    
    if(action == "add"):                                                                            # if user wants to add item to cart
        print("\nThese items are currently available:")
        displayItems(availableItems)
        item = input("What item would you like to add to cart?: ")
        item = item.upper()
        if(item in availableItems):
            cart.append(item)
            availableItems.remove(item)
            print(item.title(), "added to cart. Your cart currently contains these items:")
            displayItems(cart)
        else:
            print("Sorry, that item is unavailable.")
    elif(action == "remove"):                                                                       # if user wants to remove item from cart
        print("\nThese items are currently in your cart:")
        displayItems(cart)
        item = input("What item would you like to remove from your cart?: ")
        item = item.upper()
        if(item in cart):
            availableItems.append(item)
            cart.remove(item)
            print(item.title(), "removed from cart. Your cart currently contains these items:")
            displayItems(cart)
        else:
            print("Sorry that item is not currently in your cart.")
    elif(action == "quit"):                                                                         # if user wants to empty their cart and start over
        availableItems.extend(cart)
        cart.clear()
        print("\nCart emptied.")
    elif(action == "leave"):                                                                        # if user is done shopping and wishes to leave
        print("\nThank you for visiting PyMarket. These are the items you have selected to buy:")
        displayItems(cart)
        isAddingItems = False
    