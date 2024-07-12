import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from kiwer_api import KiwerAPI
from kiwer_driver import KiwerDriver

TEST_ID = 'kiwer'
TEST_PASSWD = '1234'
TEST_CODE = 'SAMSUNG'
BUY_PRICE = 100
BUY_COUNT = 3
SELL_PRICE = 110
SELL_COUNT = 3


class TestKiwerDriver(TestCase):
    def setUp(self):
        self.kiwer_driver = KiwerDriver()

    def test_login(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.kiwer_driver.login(TEST_ID, TEST_PASSWD)
        self.assertEqual(f'{TEST_ID} login success\n', captured_output.getvalue())

    def test_buy(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.kiwer_driver.buy(TEST_CODE, BUY_PRICE, BUY_COUNT)
        self.assertEqual(
            f'{TEST_CODE} : Buy stock ( {BUY_PRICE} * {BUY_COUNT}\n',
            captured_output.getvalue()
        )

    def test_sell(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.kiwer_driver.sell(TEST_CODE, SELL_PRICE, SELL_COUNT)
        self.assertEqual(
            f'{TEST_CODE} : Sell stock ( {SELL_PRICE} * {SELL_COUNT}\n',
            captured_output.getvalue()
        )

    @patch.object(KiwerAPI, 'current_price', return_value=BUY_PRICE)
    def test_get_price(self, mock):
        current_price = self.kiwer_driver.get_price(TEST_CODE)
        self.assertEqual(BUY_PRICE, current_price)

    @patch.object(KiwerAPI, 'current_price', return_value=SELL_PRICE)
    def test_get_price_after_3(self, mock):
        current_price = self.kiwer_driver.get_price(TEST_CODE, 3)
        self.assertEqual(SELL_PRICE, current_price)
