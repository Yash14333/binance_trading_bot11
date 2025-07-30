from binance.client import Client
from binance.enums import *
from config import API_KEY, API_SECRET, BASE_URL
from logger import log_info, log_error

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = BASE_URL + "/fapi"

        try:
            self.client.ping()
            log_info("✅ Connected to Binance Futures Testnet")
        except Exception as e:
            log_error(f"❌ Connection failed: {e}")
            exit()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            elif order_type == "STOP_MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                    type=ORDER_TYPE_STOP_MARKET,
                    stopPrice=price,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity
                )
            else:
                log_error("Unsupported order type.")
                return

            log_info(f"✅ Order placed: {order}")
        except Exception as e:
            log_error(f"❌ Order failed: {e}")
