from abc import ABC, abstractmethod


class IStockerDriver(ABC):
    @abstractmethod
    def login(self, id: str, password: str) -> None:
        pass

    @abstractmethod
    def buy(self, code: str, price: int, cnt: int) -> None:
        pass

    @abstractmethod
    def sell(self, code: str, price: int, cnt: int) -> None:
        pass

    @abstractmethod
    def get_current_price(self, code: str) -> int:
        pass
