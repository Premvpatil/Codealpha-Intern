# ✅ TASK 2: Stock Portfolio Tracker

# ● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock
# prices.
# ● Simplified Scope:
# ○ User inputs stock names and quantity.
# ○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
# ○ Display total investment value and optionally save the result in a .txt or .csv file.
# ● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling (optional).

# Available Shares
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 320
}

portfolio = {}

# ✅ Show available options
print("📈 Available Stocks and Prices:")
for symbol, price in stock_prices.items():
    print(f"{symbol} - Rs.{price}")
print("-" * 40)

# User input
num_stocks = int(input("How many stocks do you want to enter? "))
for _ in range(num_stocks):
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {symbol}: "))
    if symbol in stock_prices:
        portfolio[symbol] = quantity
    else:
        print(f"❌ {symbol} is not in the available stock list.")

# Calculate total investment
total_value = 0
for symbol, quantity in portfolio.items():
    price = stock_prices[symbol]
    value = price * quantity
    total_value += value
    print(f"{symbol}: {quantity} × ₹{price} = ₹{value}")

# Show total
print(f"\n💰 Total Investment Value: ₹{total_value}")

# Optionally write to file
with open("portfolio_report.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value = price * quantity
        file.write(f"{symbol}: {quantity} x Rs.{price} = Rs.{value}\n")
    file.write(f"\nTotal Investment Value: Rs.{total_value}\n")

print("✅ Tranjaction Logs are Saved to 'portfolio_report'.")



