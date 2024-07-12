from unittest import TestCase
from unittest.mock import Mock

class TestAutoTradingSystem(TestCase) :

    def test_select_stock_brocker(self):
        mk = Mock()
        mk.select_stock.side_effect = ['kiwer', 'nemo']
        print(mk.select_stock('kiwer'))
        mk.select_stock.assert_called()

    def test_login_brocker(self):
        pass

    def test_buy_stock(self):
        pass

    def test_sell_stock(self):
        pass

    def test_get_price_stock(self):
        pass

    def test_buy_nice_timing(self):
        pass

    def test_sell_nice_timing(self):
        pass