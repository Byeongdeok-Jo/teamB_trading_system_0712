from unittest import TestCase
from unittest.mock import Mock, patch

from Mock_driver import MockDriver
from auto_trading_system import AutoTradingSystem
from kiwer_driver import KiwerDriver
from nemo_driver import NemoDriver

STOCK_CODE_SAMSUNG = 'A005930'
STOCK_CODE_HYNIX = '000660'

INIT_BUDGET = 1000000


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
        self.sut.buy(STOCK_CODE_SAMSUNG, 2, 3)

        self.stock_driver.buy.assert_called()

    def test_sell_stock(self):
        self.sut.sell(STOCK_CODE_SAMSUNG, 100, 50)

        self.stock_driver.sell.assert_called()

    def test__successful_get_price_stock(self):
        stock_code_list = [
            STOCK_CODE_SAMSUNG,
            STOCK_CODE_SAMSUNG,
            STOCK_CODE_SAMSUNG,
            STOCK_CODE_HYNIX,
            STOCK_CODE_HYNIX,
            STOCK_CODE_HYNIX
        ]
        for code in stock_code_list:
            self.sut.get_price(code)

        self.assertEqual(6, self.stock_driver.get_price.call_count)

    def test_buy_nice_timing(self):
        self.stock_driver.get_price.side_effect = [1000, 2000, 3000, 4000]
        self.sut.buy_nice_timing(STOCK_CODE_HYNIX, 2000)

        self.stock_driver.buy.assert_called_once()

    def test_sell_nice_timing(self):
        self.stock_driver.get_price.side_effect = [3000, 2000, 1000, 0]
        self.sut.sell_nice_timing(STOCK_CODE_HYNIX, 5)

        self.stock_driver.sell.assert_called_once()

    def test_correct_stock_code(self):
        self.assertIsNotNone(self.sut.get_price(STOCK_CODE_SAMSUNG))
        self.assertIsNotNone(self.sut.get_price(STOCK_CODE_HYNIX))

    def test_incorrect_stock_code(self):
        invalid_stock_codes = ['1234', '41231', 'AA12334', 'D12345']
        for invalid_stock_code in invalid_stock_codes:
            self._assert_raise_for_get_price(invalid_stock_code)

    def _assert_raise_for_get_price(self, invalid_stock_code):
        with self.subTest(f"Invalid stock code test {invalid_stock_code}"):
            with self.assertRaises(Exception):
                self.sut.get_price(invalid_stock_code)

    def test_get_init_budget(self):
        self.assertEqual(self.get_current_money_budget(), INIT_BUDGET)
        self.assertEqual(self.get_current_stock_budget(), 0)

    def test_buget_updated_correctly_after_buy(self):
        self.stock_driver.get_price.return_value = 5000
        self.sut.buy(STOCK_CODE_SAMSUNG, 5000, 2)
        self.assertEqual(self.get_current_money_budget(), INIT_BUDGET - 5000 * 2)
        self.assertEqual(self.get_current_stock_budget(), 5000 * 2)

    def test_cannot_buy_anymore(self):
        self.sut.buy(STOCK_CODE_SAMSUNG, 5000, 100)
        self.sut.buy(STOCK_CODE_SAMSUNG, 5000, 104)
        self.assertEqual(self.get_current_money_budget(), INIT_BUDGET - 5000 * 100)

    def test_cannot_sell_before_buy(self):
        with self.assertRaises(Exception):
            self.sut.sell(STOCK_CODE_SAMSUNG, 5000, 1000)

    def test_updated_correctly_after_buy_and_sell(self):
        self.sut.buy(STOCK_CODE_SAMSUNG, 5000, 2)
        self.sut.sell(STOCK_CODE_SAMSUNG, 5000, 1)
        self.assertEqual(self.get_current_money_budget(), INIT_BUDGET - 5000)

    def get_current_money_budget(self):
        return self.sut.get_current_budget()[0]

    def get_current_stock_budget(self):
        return self.sut.get_current_budget()[1]
