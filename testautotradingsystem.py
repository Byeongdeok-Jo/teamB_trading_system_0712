from unittest import TestCase
from unittest.mock import Mock, patch
from autotradingsystem import AutoTradingSystem


class TestAutoTradingSystem(TestCase):
    def setUp(self):
        super().setUp()
        self.sut = AutoTradingSystem()

    @patch.object(AutoTradingSystem, 'select_stock_brocker', return_value='kiwer')
    def test_select_stock_brocker(self, mk_select_storck_brocker):
        self.sut.select_stock_brocker('kiwer')
        mk_select_storck_brocker.assert_called()

    @patch.object(AutoTradingSystem, 'login')
    def test_login_brocker(self, mk_login):
        self.sut.login('test12', 1234)
        mk_login.assert_called()

    @patch.object(AutoTradingSystem, 'buy')
    def test_buy_stock(self, mk_buy):
        self.sut.buy(1234, 100, 50)
        mk_buy.assert_called()

    @patch.object(AutoTradingSystem, 'sell')
    def test_sell_stock(self, mk_sell):
        self.sut.sell(1234, 100, 50)
        mk_sell.assert_called()

    @patch.object(AutoTradingSystem, 'current_price')
    def test__successful_get_price_stock(self, mk_current_price):
        stock_code_list = [1234, 2345, 3456, 4567, 1234, 1111]
        for code in stock_code_list:
            self.sut.current_price(code)
        self.assertEqual(6, mk_current_price.call_count)

    def test_buy_nice_timing(self):
        pass

    def test_sell_nice_timing(self):
        pass

    @patch.object(KiwerDriver, 'get_price', side_effect=[1000, 2000, 3000])
    def test_buy_nice_timing_kiwer(self, mk_driver):
        self.sut.select_stock_brocker('kiwer')
        self.sut.buy_nice_timing(1234, 2000)
        self.assertEqual(mk_driver.buy_nice_timing.call_count, 1)

    @patch.object(KiwerDriver, 'get_price', side_effect=[3000, 2000, 1000])
    def test_sell_nice_timing_from_kiwer(self, mk_driver):
        self.sut.select_stock_brocker('kiwer')
        self.sut.sell_nice_timing(1234, 5)
        self.assertEqual(mk_driver.sell_nice_timing.call_count, 1)
