from unittest import TestCase
from unittest.mock import Mock, patch

from Mock_driver import MockDriver
from auto_trading_system import AutoTradingSystem


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
        pass

    def test_sell_nice_timing(self):
        pass

    def test_login_mock(self):
        self.mock_driver.login('test_user', 'test_pass')
        self.assertIn('Logged in as test_user', self.mock_driver.actions)

    def test_buy_mock(self):
        self.mock_driver.buy('AAPL', 150, 10)
        self.assertIn('Bought 10 of AAPL at 150', self.mock_driver.actions)

    def test_sell_mock(self):
        self.mock_driver.sell('AAPL', 155, 5)
        self.assertIn('Sold 5 of AAPL at 155', self.mock_driver.actions)

    def test_get_price_mock(self):
        price = self.mock_driver.get_price('AAPL')
        self.assertEqual(price, 5500)

    # def test_buy_nice_timing(self):
    #     self.mock_driver.set_mock_price(500)
    #     self.app.buy_nice_timing('AAPL', 1000)
    #     self.assertIn('Bought 2 of AAPL at 500', self.mock_driver.actions)
    #
    # def test_sell_nice_timing(self):
    #     self.mock_driver.set_mock_price(600)
    #     self.app.sell_nice_timing('AAPL', 3)
    #     self.assertIn('Sold 3 of AAPL at 600', self.mock_driver.actions)
