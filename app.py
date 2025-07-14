def calculate_discount(price, discount):
    return price - (price * discount)

def calculate_tax(price, tax_rate):
    return price + (price * tax_rate)

def main():
    print("Welcome to our pricing app!")
    discounted_price = calculate_discount(100, 0.1)
    final_price = calculate_tax(discounted_price, 0.05)
    print("Final price with tax:", final_price)
