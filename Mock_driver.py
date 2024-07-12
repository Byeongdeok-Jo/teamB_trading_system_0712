from stock_driver import IStockDriver

class MockDriver(IStockDriver):
    def __init__(self):
        self.logged_in = False
        self.actions = []
        self.mock_price = 5500
        self.call_count = {
            "login": 0,
            "buy": 0,
            "sell": 0,
            "get_price": 0
        }

    def login(self, id, password):
        self.logged_in = True
        self.actions.append(f"Logged in as {id}")
        self.call_count["login"] += 1

    def buy(self, stock_code, price, count):
        self.actions.append(f"Bought {count} of {stock_code} at {price}")
        self.call_count["buy"] += 1

    def sell(self, stock_code, price, count):
        self.actions.append(f"Sold {count} of {stock_code} at {price}")
        self.call_count["sell"] += 1

    def get_price(self, stock_code, minute=0):
        self.call_count["get_price"] += 1
        return self.mock_price

    def set_mock_price(self, price):
        self.mock_price = price

