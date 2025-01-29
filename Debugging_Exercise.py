def calculate_discount(price, discount_rate):
    """Calculate the discount amount based on the price and discount rate."""
    return price * discount_rate

def apply_discount(price, discount_amount):
    """Apply the discount amount to the original price and return the new price."""
    return price - discount_amount

def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},  # Incorrect type
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        try:
            price = float(product["price"])  # Convert to float to handle incorrect types
            discount_rate = product["discount_rate"]

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price:.2f}")
            print(f"Discount Amount: ${discount_amount:.2f}")
            print(f"Final Price: ${final_price:.2f}")
            print()

        except ValueError:
            print(f"Error: Invalid price format for {product['name']}. Expected a number.")
        except TypeError:
            print(f"Error: Invalid type detected in product data for {product['name']}.")

if __name__ == "__main__":
    main()
