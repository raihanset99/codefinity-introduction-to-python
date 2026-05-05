def apply_discount(prices):
    # 1. Copy the original list
    prices_copy = prices.copy()
    # 2. Apply 10% discount to items > $2.00
    for i in range(len(prices_copy)):
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.90
    # 3. Return new list
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

# Print the updated prices
print(f"Updated product prices: {updated_prices}")