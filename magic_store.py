import warnings


def add_to_cart(item, cart):
    # Adds an item to the cart if it's not already there.
    if item in cart:
        # Issue a warning if the item is already in the cart
        warnings.warn(f"{item} is already in the cart!", UserWarning)
        return f"{item} is already in the cart!"
    cart.append(item)
    return f"{item} has been added to the cart."

def checkout(cart):
    # Checks out the cart if it contains items.
    if len(cart) > 0:
        return f"Checking out with {len(cart)} items!"
    return "Your cart is empty! Add some magic items first!"

# Calling the functions
# cart = []

# # Adding items to the cart
# print(add_to_cart("Magic Wand", cart))  
# print(add_to_cart("Flying Broom", cart)) 
# print(add_to_cart("Invisibility Cloak", cart)) 
# print(add_to_cart("Magic Wand", cart))  