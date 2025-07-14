import logging

logging.basicConfig(level=logging.INFO)

def calculate_discount(price, discount):
    if discount > 1 or discount < 0:
        raise ValueError("Discount must be between 0 and 1")
    logging.info(f"Calculating discount: price={price}, discount={discount}")
    return price - (price * discount)

def calculate_tax(price, tax_rate):
    return price + (price * tax_rate)

def main():
    print("Welcome to our pricing app!")

    try:
        discounted_price = calculate_discount(100, 0.1)
        final_price = calculate_tax(discounted_price, 0.05)
        print("Final price with tax:", final_price)
    except ValueError as e:
        logging.error(f"Error: {e}")

