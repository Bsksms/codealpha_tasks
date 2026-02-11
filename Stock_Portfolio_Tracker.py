
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "AMZN": 175.00,
    "MSFT": 400.00
}

def calculate_portfolio():
    print("--- Stock Portfolio Tracker ---")
    print(f"Available Stocks: {', '.join(STOCK_PRICES.keys())}\n")
    
    portfolio = {}
    total_value = 0.0

    while True:
        symbol = input("Enter stock symbol (or type 'done' to finish): ").upper()
        
        if symbol == 'DONE':
            break
        
        if symbol in STOCK_PRICES:
            try:
                quantity = int(input(f"How many shares of {symbol} do you own? "))
                price = STOCK_PRICES[symbol]
                investment = quantity * price
                
                portfolio[symbol] = {"quantity": quantity, "value": investment}
                total_value += investment
                print(f"Added: {symbol} | Value: ₹{investment:,.2f}")
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")
        else:
            print(f"Sorry, {symbol} is not in our database.")

    
    print("\n" + "="*30)
    print("FINAL PORTFOLIO SUMMARY")
    print("="*30)
    
    summary_text = "Stock | Quantity | Total Value\n"
    summary_text += "-" * 30 + "\n"
    
    for stock, data in portfolio.items():
        line = f"{stock: <6} | {data['quantity']: <8} | ₹{data['value']:,.2f}\n"
        summary_text += line
        print(line.strip())

    final_total = f"\nTOTAL PORTFOLIO VALUE: ₹{total_value:,.2f}"
    summary_text += final_total
    print(final_total)

    
    save_choice = input("\nWould you like to save this report to a file? (y/n): ").lower()
    if save_choice == 'y':
        with open("portfolio_report.txt", "w") as file:
            file.write(summary_text)
        print("Report saved to 'portfolio_report.txt'!")

if __name__ == "__main__":
    calculate_portfolio()
