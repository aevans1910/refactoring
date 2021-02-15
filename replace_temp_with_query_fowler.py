# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
def calculate_price(quantity, item_price):
    base_price = quantity * item_price
    return base_price
def get_price(base_price):
    discount_factor = 0
    if base_price > 1000: 
        discount_factor = 0.95
    else: 
        discount_factor = 0.98
    return base_price * discount_factor
print(calculate_price(5, 5.50))
print(get_price(6))