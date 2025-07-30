from bot import BasicBot

def get_input():
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    order_type = input("Enter order type (MARKET / LIMIT / STOP_MARKET): ").upper()
    quantity = float(input("Enter quantity: "))
    price = None

    if order_type in ["LIMIT", "STOP_MARKET"]:
        price = input("Enter price or stopPrice: ")

    return symbol, side, order_type, quantity, price

if __name__ == "__main__":
    bot = BasicBot(api_key="your_testnet_api_key", api_secret="your_testnet_api_secret")

    symbol, side, order_type, quantity, price = get_input()
    bot.place_order(symbol, side, order_type, quantity, price)
