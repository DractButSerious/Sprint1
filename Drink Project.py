# Create class "Drink"
class Drink:
    # Initialize the valid bases and flavors.
    _valid_bases = {"Water", "Sprite", "Coca-Cola", "Dr. Pepper", "Starry", "Root Beer"}
    _valid_flavors = {"Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", "Lime"}

    # Initialize with no base and an empty flavor list.
    def __init__(self):
        self._base = None
        self._flavors = set()

    # Return the _base property.
    def get_base(self):
        return self._base
    
    # Return the _flavors property.
    def get_flavors(self):
        return list(self._flavors)
    
    # Return the number of flavors.
    def get_num_flavors(self):
        return len(self._flavors)
    
    # Set the drink's _base property.
    def set_base(self, base):
        if base in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"Pick a proper base from {self._valid_bases}.")
    
    # Add a flavor to the _flavors property.
    def add_flavor(self, flavor):
        if flavor in self._valid_flavors:
            self._flavors.add(flavor)
        else:
            raise ValueError(f"Pick a proper flavor from {self._valid_flavors}.")

    # Set the _flavors property to a given list.
    def set_flavors(self, flavors):
        for flavor in flavors:
            if flavor not in self._valid_flavors:
                raise ValueError(f"Pick a proper flavor from {self._valid_flavors}.")
        self._flavors = set(flavors)


# Create class "Order"
class Order:
    # Give the class instance its _items property.
    def __init__(self):
        self._items = []
    
    # Return the list of items in this instance.
    def get_items(self):
        return self._items

    # Return the number of items in this instance.
    def get_total(self):
        return len(self._items)
    
    # List out every item in the list.
    def get_receipt(self):
        receipt = "Your order receipt:\n"
        for i, drink in enumerate(self._items):
            base = drink.get_base()
            # Formats the "flavors" string like "Lemon, Mint, Blueberry"
            flavors = ", ".join(drink.get_flavors())
            # Example: "1: Base - Root Beer, Flavors - Lemon, Cherry"
            receipt += f"{i + 1}: Base - {base}, Flavors - {flavors}\n"
        return receipt
    
    # Add a Drink instance to the end of the list.
    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            # If the instance is not a Drink, throw an error.
            raise ValueError("You can only add drinks to this order.")
    
    # Remove a Drink instance from the list based on index.
    def remove_item(self, index):
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            # If the index is outside of the list, i.e. invalid, throw an error.
            raise IndexError("Invalid index, cannot remove item.")