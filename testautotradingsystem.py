from unittest.mock import Mock, patch
from autotradingsystem import AutoTradingSystem
from Mock_driver import MockDriver


class TestAutoTradingSystem(TestCase) :
    def setUp(self):
        super().setUp()
        self.sut = AutoTradingSystem()
        self.mock_driver = MockDriver()

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

    @patch.object(MockDriver, 'get_price', side_effect=[1000, 2000, 3000])
    def test_buy_nice_timing(self, mk_driver):
        self.sut.buy_nice_timing(1234, 2000)
        self.assertEqual(mk_driver.buy_nice_timing.call_count, 1)

    @patch.object(MockDriver, 'get_price', side_effect=[3000, 2000, 1000])
    def test_sell_nice_timing(self, mk_driver):
        self.sut.sell_nice_timing(1234, 5)
        self.assertEqual(mk_driver.sell_nice_timing.call_count, 1)

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
