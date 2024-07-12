from stock_driver import IStockDriver


class MockDriver(IStockDriver):
    def __init__(self):
        self.logged_in = False
        self.actions = []
        self.mock_price = 5500

    def login(self, id, password):
        pass

    def buy(self, stock_code, price, count):
        pass

    def sell(self, stock_code, price, count):
        pass

    def get_price(self, stock_code, minute=0):
        pass

    def set_mock_price(self, price):
        pass
