def main():
    import sys

    if len(sys.argv) != 4:
        print("Usage: python app.py <price> <discount> <tax_rate>")
        return

    try:
        price = float(sys.argv[1])
        discount = float(sys.argv[2])
        tax_rate = float(sys.argv[3])

        discounted_price = calculate_discount(price, discount)
        final_price = calculate_tax(discounted_price, tax_rate)
        print("Final price with tax:", final_price)
    except ValueError as e:
        logging.error(f"Invalid input: {e}")

