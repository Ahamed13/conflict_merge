def main():
    print("Welcome to our pricing app!")
    try:
        discounted_price = calculate_discount(100, 0.1)
        final_price = calculate_tax(discounted_price, 0.05)
        print("Final price with tax:", final_price)
    except ValueError as e:
        logging.error(f"Error: {e}")

