from stock_driver import IStockDriver


class AutoTradingSystem:
    _stock_driver: IStockDriver

    def select_stock_broker(self):
        pass

    def set_stock_driver(self, stock_driver):
        self._stock_driver = stock_driver

    def get_stock_driver(self):
        return self._stock_driver

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
