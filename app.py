import logging

logging.basicConfig(level=logging.INFO)

def calculate_discount(price, discount):
    if discount > 1 or discount < 0:
        raise ValueError("Discount must be between 0 and 1")
    logging.info(f"Calculating discount: price={price}, discount={discount}")
    return price - (price * discount)

def main():
    print("Welcome to our pricing app!")
    try:
        final = calculate_discount(100, 0.1)
        print("Final price:", final)
    except ValueError as e:
        logging.error(f"Error: {e}")
