# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 190,
    "GOOGL": 175,
    "MSFT": 420,
    "AMZN": 185,
    "TSLA": 210
}

portfolio = {}
total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter Stock Symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available in database.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value

    print(f"{stock}")
    print(f"Quantity: {quantity}")
    print(f"Price: ${stock_prices[stock]}")
    print(f"Value: ${value}")
    print("-" * 30)

print(f"\nTotal Portfolio Value: ${total_value}")

# Save Report
with open("portfolio_report.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 30 + "\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity

        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Price: ${stock_prices[stock]}\n")
        file.write(f"Value: ${value}\n")
        file.write("-" * 30 + "\n")

    file.write(f"\nTotal Portfolio Value: ${total_value}")

print("\nPortfolio report saved as 'portfolio_report.txt'")