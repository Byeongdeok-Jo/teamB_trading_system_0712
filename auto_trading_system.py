from stock_driver import IStockDriver


class AutoTradingSystem:
    _stock_driver: IStockDriver

    def select_stock_broker(self, name: str):
        self._stock_driver = self.create_stock_driver_from_name(name)

    def set_stock_driver(self, stock_driver):
        self._stock_driver = stock_driver

    def get_stock_driver(self):
        return self._stock_driver

    def create_stock_driver_from_name(self, name: str):
        raise NotImplementedError()

    def login(self, id, passwd):
        self._stock_driver.login(id, passwd)

    def buy(self, stock_code, price, count):
        self._stock_driver.buy(stock_code, price, count)

    def sell(self, stock_code, price, count):
        self._stock_driver.sell(stock_code, price, count)

    def get_price(self, stock_code) -> int:
        return self._stock_driver.get_price(stock_code, 0)

    def buy_nice_timing(self, stock_code, budget):
        if self._is_nice_time_to_buy(stock_code):
            self._buy_up_to_budget(budget, stock_code)

    def _buy_up_to_budget(self, budget, stock_code):
        current = self.get_price(stock_code)
        buy_count = budget // current
        self._stock_driver.buy(stock_code, current, buy_count)

    def sell_nice_timing(self, stock_code, count):
        if self._is_nice_timing_to_sell(stock_code):
            self._stock_driver.sell(stock_code, self.get_price(stock_code), count)

    def _is_nice_time_to_buy(self, stock_code):
        prev_2min = self._stock_driver.get_price(stock_code, 2)
        prev_1min = self._stock_driver.get_price(stock_code, 1)
        current = self._stock_driver.get_price(stock_code, 0)
        time_to_buy = prev_2min < prev_1min < current
        return time_to_buy

    def _is_nice_timing_to_sell(self, stock_code):
        prev_2min = self._stock_driver.get_price(stock_code, 2)
        prev_1min = self._stock_driver.get_price(stock_code, 1)
        current = self._stock_driver.get_price(stock_code, 0)
        time_to_sell = prev_2min > prev_1min > current
        return time_to_sell
