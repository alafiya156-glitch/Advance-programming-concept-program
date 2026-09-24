# discount_module.py

def calculate_discount(price, discount):
    return price * discount / 100


def final_price(price, discount):
    amount = calculate_discount(price, discount)
    return price - amount

