"""
Problem Statement:
Write a Python program that simulates a receipt/billing system for a store.
The program should allow the user to enter multiple product purchases, 
group them by category, calculate totals, and print a formatted receipt.

Requirements:
1. Repeatedly ask the user if they want to enter a new product.
2. For each product, collect:
   - Product Category (e.g., Grocery, Electronics)
   - Product Name
   - Quantity purchased
   - Price per item
3. Validate:
   - Quantity must be a positive integer
   - Price must be a positive number
4. Group all products under their categories.
5. Calculate:
   - Subtotal (sum of all product prices × quantities)
   - Tax (6%)
   - Total after tax
   - Change (Paid amount – total)
6. Print a formatted receipt showing:
   - Date and time
   - Total items purchased
   - Category-wise product list
   - Subtotal, tax, total, paid amount, change
"""

import datetime
import locale

# Use system locale for currency formatting (if available)
locale.setlocale(locale.LC_ALL, "")
currency_symbol = locale.localeconv().get("currency_symbol", "$")

today = datetime.datetime.today()


class ReceiptFormatter:
    """
    Class to store products, quantities, prices and to print a formatted receipt.
    """
    def __init__(self):
        self.product_categories = {}  # {category: {product_name: Product}}
        self.total_price = 0.0
        self.total_quantity = 0

    def print_header(self):
        print("*" * 5 + " RECEIPT " + "*" * 5)
        print(today.strftime("%d/%m/%Y"), today.strftime("%I:%M %p"))
        print("*" * 40)
        print("{:<24} {:>13}".format("Total items", self.total_quantity))
        print("*" * 40)
        print("{:<4}{:<20} {:>6} {:>6}".format("Cat", "Product", "Qty", "Price"))


class Product:
    def __init__(self, product_name, product_quantity, product_price):
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price


def get_cost_details():
    """
    Reads product details from the user and prints a formatted receipt.
    """
    quit_flag = "no"
    receipt = ReceiptFormatter()

    while quit_flag.lower() == "no":
        quit_flag = input("Do you want to quit? (yes or no): ").strip().lower()

        if quit_flag == "no":
            category = input("Enter the Category: ")
            product = input("Enter the Product: ")
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: "))

            if price < 0 or quantity <= 0:
                print("Please give proper positive quantity and cost.")
                continue

            # If category already exists
            if category in receipt.product_categories:
                # If product already exists under the category
                if product in receipt.product_categories[category]:
                    product_obj = receipt.product_categories[category][product]
                    product_obj.product_quantity += quantity
                else:
                    product_obj = Product(product, quantity, price)
                    receipt.product_categories[category][product] = product_obj
            else:
                receipt.product_categories[category] = {}
                receipt.product_categories[category][product] = Product(product, quantity, price)

            receipt.total_price += quantity * price
            receipt.total_quantity += quantity

    # Printing receipt
    if receipt.total_quantity > 0:
        after_tax = receipt.total_price * 1.06
        paid_price = float(input("Enter the amount paid: "))

        receipt.print_header()

        # Print categories and products
        for category, products in receipt.product_categories.items():
            print(category)
            for product_name, prod_obj in products.items():
                subtotal = prod_obj.product_quantity * prod_obj.product_price
                print("    {:<20} {:>6} {:>6}".format(
                    product_name,
                    prod_obj.product_quantity,
                    currency_symbol + str(subtotal)
                ))

        # Summary
        print("{:<24} {:>13}".format("Subtotal", currency_symbol + str(round(receipt.total_price, 2))))
        print("{:<24} {:>13}".format("Tax", currency_symbol + str(round(receipt.total_price * 0.06, 2))))
        print("*" * 40)
        print("{:<24} {:>13}".format("Total", currency_symbol + str(round(after_tax, 2))))
        print("{:<24} {:>13}".format("Paid", currency_symbol + str(paid_price)))
        print("*" * 40)
        print("{:<24} {:>13}".format("Change", currency_symbol + str(round(paid_price - after_tax, 2))))


# Run the program
get_cost_details()

