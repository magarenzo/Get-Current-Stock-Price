from yahoo_fin import stock_info

# Prompt user to input stock ticker and get current live price
while True:
    try:
        ticker = input("\nWhat is the stock ticker? ")
        price = str(stock_info.get_live_price(ticker))
        break
    except:
        print("No data found, symbol may be delisted.")

# Print
print("\nThe current live price of stock $" + str.upper(ticker) + " is $" + price + ".")