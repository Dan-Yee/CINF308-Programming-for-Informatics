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
Class to represent a store
"""
class Store:
    def __init__(self) -> None:
        self.shelf = list()
    
    def addToShelf(self, item : StoreItem) -> None:
        self.shelf.append(item)

    def removeFromShelf(self, item: StoreItem) -> None:
        self.shelf.remove(item)

"""
Class to represent a shopping cart in a store
"""
class Cart:
    def __init__(self) -> None:
        self.cart = list()
        self.total = 0

    """
    Class function to add an item to a cart if it exists
    Returns true if the item was added and false otherwise
    """
    def addToCart(self, item : StoreItem) -> None:
        self.cart.append(item)
    
    """
    Class function to remove an item from the cart
    Returns true if the item was removed and false otherwise
    """
    def RemoveFromCart(self, item : StoreItem) -> None:
        self.cart.remove(item)


##################################################
