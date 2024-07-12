from unittest import TestCase
from unittest.mock import Mock, patch
from Mock_driver import MockDriver
from auto_trading_system import AutoTradingSystem
from kiwer_driver import KiwerDriver
from nemo_driver import NemoDriver


class TestAutoTradingSystem(TestCase):
    def setUp(self):
        super().setUp()
        self.sut = AutoTradingSystem()
        self.mock_driver = MockDriver()
        self.stock_driver = Mock()  # TODO: Replace Mock() with MockDriver
        self.sut.set_stock_driver(self.stock_driver)

    @patch.object(AutoTradingSystem, 'create_stock_driver_from_name', return_value=Mock())
    def test_select_stock_broker(self, create_mk):
        self.sut.set_stock_driver(None)
        self.sut.select_stock_broker('kiwer')

        create_mk.assert_called_once()
        self.assertIsNotNone(self.sut.get_stock_driver())

    def test_can_select_kiwer_driver(self):
        self.sut.select_stock_broker('kiwer')
        self.assertIsInstance(self.sut.get_stock_driver(), KiwerDriver)

    def test_can_select_nemo_driver(self):
        self.sut.select_stock_broker('nemo')
        self.assertIsInstance(self.sut.get_stock_driver(), NemoDriver)

    def test_login_brocker(self):
        self.sut.login('test12', 1234)
        self.stock_driver.login.assert_called()

    def test_buy_stock(self):
        self.sut.buy(1, 2, 3)
        self.stock_driver.buy.assert_called()

    def test_sell_stock(self):
        self.sut.sell(1234, 100, 50)
        self.stock_driver.sell.assert_called()

    def test__successful_get_price_stock(self):
        stock_code_list = [1234, 2345, 3456, 4567, 1234, 1111]
        for code in stock_code_list:
            self.sut.get_price(code)
        self.assertEqual(6, self.stock_driver.get_price.call_count)

    def test_buy_nice_timing(self):
        self.stock_driver.get_price.side_effect = [1000, 2000, 3000, 4000]
        self.sut.buy_nice_timing(1234, 2000)
        self.stock_driver.buy.assert_called_once()

    def test_sell_nice_timing(self):
        self.stock_driver.get_price.side_effect = [3000, 2000, 1000, 0]
        self.sut.sell_nice_timing(1234, 5)
        self.stock_driver.sell.assert_called_once()
