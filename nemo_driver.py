from stock_driver import IStockDriver
from nemo_api import NemoAPI

class NemoDriver(IStockDriver):
    def __init__(self):
        self.__nemo_handler = NemoAPI()

    def login(self, id, pwd):
        return self.__nemo_handler.certification(id, pwd)

    def buy(self, stock_code, price, count):
        return self.__nemo_handler.purchasing_stock(stock_code, price, count)

    def sell(self, stock_code, price, count):
        return self.__nemo_handler.selling_stock(stock_code, price, count)

    def get_price(self, stock_code, minute):
        return self.__nemo_handler.get_market_price(stock_code, minute)
