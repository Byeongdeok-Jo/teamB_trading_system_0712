from stock_driver import IStockDriver


class MockDriver(IStockDriver):
    def __init__(self):
        self.logged_in = False
        self.actions = []
        self.mock_price = 5500

    def login(self, id, password):
        self.logged_in = True
        self.actions.append(f"Logged in as {id}")

    def buy(self, stock_code, price, count):
        self.actions.append(f"Bought {count} of {stock_code} at {price}")

    def sell(self, stock_code, price, count):
        self.actions.append(f"Sold {count} of {stock_code} at {price}")

    def get_price(self, stock_code, minute=0):
        return self.mock_price

    def set_mock_price(self, price):
        self.mock_price = price
