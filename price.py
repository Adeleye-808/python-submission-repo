def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Get user inputs
price = float(input("Enter the original price of the item (in Naira): "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Format price with Naira symbol and comma separators
def format_naira(amount):
    return f"₦{amount:,.2f}"

# Print final price or original price
if discount_percent >= 20:
    print(f"Discount applied. Final price: {format_naira(final_price)}")
else:
    print(f"No discount applied. Original price remains: {format_naira(price)}")
