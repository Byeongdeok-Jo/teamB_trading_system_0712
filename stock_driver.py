from abc import ABC, abstractmethod


class IStockDriver(ABC):
    @abstractmethod
    def login(self, id, password):
        pass

    @abstractmethod
    def buy(self, stock_code, count, price):
        pass

    @abstractmethod
    def sell(self, stock_code, count, price):
        pass

    @abstractmethod
    def get_price(self, stock_code, minute=0) -> int:
        pass
