import time

from stock_driver import IStockDriver
from kiwer_api import KiwerAPI


class KiwerDriver(IStockDriver):
    def __init__(self):
        self.__kiwer_handler = KiwerAPI()

    def login(self, id, passwd):
        return self.__kiwer_handler.login(id, passwd)

    def buy(self, stocker_code, price, count):
        return self.__kiwer_handler.buy(stocker_code, count, price)

    def sell(self, stocker_code, price, count):
        return self.__kiwer_handler.sell(stocker_code, count, price)

    def get_price(self, stock_code, minute=0) -> int:
        if minute <= 0:
            minute = 1
        time.sleep(minute / 1000)
        return self.__kiwer_handler.current_price(stock_code)
