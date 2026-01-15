def portfolio_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 320
    }

    total_value = 0

    print("Stock Portfolio Tracker")
    print("Type 'done' to finish.\n")

    while True:
        stock = input("Enter stock symbol: ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity.")
            continue

        value = stock_prices[stock] * quantity
        total_value += value

        print(f"Added {stock}: ₹{value}\n")

    print("Total Investment Value: ₹", total_value)


portfolio_tracker()
