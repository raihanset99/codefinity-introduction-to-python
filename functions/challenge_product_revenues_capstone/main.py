# Task 1: Define a function to calculate the revenue for each product
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for idx in range(len(prices)):
        revenue.append(prices[idx] * quantities_sold[idx])
    return revenue

# Task 2: Define a function to format and display the sorted revenues
def formatted_output(revenues):
    for name, rev in sorted(revenues, key=lambda pair: pair[0]):
        print(f"{name} has total revenue of ${rev}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Task 3: Call the functions and display results
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)