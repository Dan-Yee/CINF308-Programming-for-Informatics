"""
Class to represent an item that can be purchased from a store
"""
class StoreItem:
    def __init__(self, name : str, price : float) -> None: 
        self.name = name.upper()
        self.price = price
    
    """
    Class function to get the name of a particular item.
    """
    def getName(self) -> str:
        return self.name.title()

    """
    Class function to get the price of an item
    """
    def getPrice(self) -> float:
        return self.price

"""
Class to represent a shopping cart in a store
"""
class Cart:
    def __init__(self) -> None:
        self.shoppingCart = list()
        self.total = 0

    """
    Class function to add an item to a cart if it exists
    Returns true if the item was added and false otherwise
    """
    def addToCart(self, item : StoreItem) -> None:
        self.shoppingCart.append(item)
        self.total += item.getPrice()
    
    """
    Class function to remove an item from the cart
    Returns true if the item was removed and false otherwise
    """
    def RemoveFromCart(self, item : StoreItem) -> None:
        self.total -= item.getPrice()
        

##################################################
cart = Cart()
availableItems = list()
availableItems.append(StoreItem("MILK", 4.33))
availableItems.append(StoreItem("EGGS", 2.90))
availableItems.append(StoreItem("BREAD", 2.50))
availableItems.append(StoreItem("WATER", 1.00))
availableItems.append(StoreItem("COFFEE", 1.18))
availableItems.append(StoreItem("POTATOES", 0.78))
availableItems.append(StoreItem("LETTUCE", 1.61))
availableItems.append(StoreItem("PASTA", 1.09))
availableItems.append(StoreItem("RICE", 1.35))
availableItems.append(StoreItem("BEANS", 1.69))

"""
Function to check for and remove an item from the shelf
"""
def availableAndRemove(item, collection):
    for product in collection:
        if product.getName() == item.title():
            collection.remove(product)
            return product
    return None

"""
Function to display items either available on the shelf (availableItems) or in the users cart (cart)
"""
def displayItems(items):
    for item in items:
        print("\t", item.getName(), " [$", format(item.getPrice(), ".2f"), "]", sep = "")

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
print("\nThese items are currently available:")
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

        itemRequest = availableAndRemove(item, availableItems)
        if itemRequest is not None:
            cart.addToCart(itemRequest)
            print("Added to Cart!")
            print("\nThese items are currently in your cart:")
            displayItems(cart.shoppingCart)
            print("All the items in your cart cost a total of $", format(cart.total, ".2f"), "\n", sep = "")
        else:
            print("Sorry, that item is unavailable.\n")
            
    elif(action == "remove"):                                                                       # if user wants to remove item from cart
        print("\nThese items are currently in your cart:")
        displayItems(cart.shoppingCart)
        item = input("What item would you like to remove from your cart?: ")
        item = item.upper()

        itemRequest = availableAndRemove(item, cart.shoppingCart)
        if itemRequest is not None:
            cart.RemoveFromCart(itemRequest)
            availableItems.append(itemRequest)
            print("Removed from Cart!")
            print("\nThese items are currently in your cart:")
            displayItems(cart.shoppingCart)
            print("All the items in your cart cost a total of $", format(cart.total, ".2f"), "\n", sep = "")
        else:
            print("Sorry that item is not currently in your cart.\n")
    elif(action == "quit"):                                                                         # if user wants to empty their cart and start over
        availableItems.extend(cart.shoppingCart)
        cart.cart.clear()
        print("\nCart emptied.\n")
    elif(action == "leave"):                                                                        # if user is done shopping and wishes to leave
        print("\nThank you for visiting PyMarket. These are the items you have selected to buy:")
        displayItems(cart.shoppingCart)
        print("All the items in your cart cost a total of $", format(cart.total, ".2f"), "\n", sep = "")
        isAddingItems = False