from stock_driver import IStockDriver


class AutoTradingSystem:
    _stock_driver: IStockDriver

    def select_stock_broker(self, name: str):
        self._stock_driver = self.create_stock_driver_from_name(name)

    def set_stock_driver(self, stock_driver):
        self._stock_driver = stock_driver

    def get_stock_driver(self):
        return self._stock_driver

    def create_stock_driver_from_name(self):
        return None

    def login(self, id, passwd):
        pass

    def buy(self, stock_code, price, count):
        pass

    def sell(self, stock_code, price, count):
        pass

    def get_price(self, stock_code):
        pass

    def buy_nice_timing(self, stock_code, budget):
        pass

    def sell_nice_timing(self, stock_code, count):
        pass
