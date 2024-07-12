from stock_driver import IStockDriver
from nemo_api import NemoAPI


class NemoDriver(IStockDriver):
    def __init__(self):
        self.__nemo_handler = NemoAPI()

    def login(self, id, passwd):
        return self.__nemo_handler.cerification(id, passwd)

    def buy(self, stocker_code, price, count):
        return self.__nemo_handler.purchasing_stock(stocker_code, price, count)

    def sell(self, stocker_code, price, count):
        return self.__nemo_handler.selling_stock(stocker_code, price, count)

    def get_price(self, stock_code, minute=0) -> int:
        return self.__nemo_handler.get_market_price(stock_code, minute)
