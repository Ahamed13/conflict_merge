def calculate_discount(price, discount):
    return price - (price * discount)

def main():
    print("Welcome to our pricing app!")
    print("Final price:", calculate_discount(100, 0.1))
