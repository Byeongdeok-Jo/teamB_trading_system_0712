from unittest import TestCase
from unittest.mock import Mock

from Mock_driver import MockDriver


class TestAutoTradingSystem(TestCase):

    def setUp(self):
        self.mock_driver = MockDriver()

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

