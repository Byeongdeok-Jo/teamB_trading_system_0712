import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from nemo_api import NemoAPI
from nemo_driver import NemoDriver

TEST_ID = 'nemo'
TEST_PASSWD = '1234'
TEST_CODE = 'SAMSUNG'
BUY_PRICE = 100
BUY_COUNT = 3
SELL_PRICE = 110
SELL_COUNT = 3


class TestNemoDriver(TestCase):
    def setUp(self):
        self.nemo_driver = NemoDriver()

    def test_login(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.nemo_driver.login(TEST_ID, TEST_PASSWD)
        self.assertEqual(f'[NEMO]{TEST_ID} login GOOD\n', captured_output.getvalue())

    def test_buy(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.nemo_driver.buy(TEST_CODE, BUY_PRICE, BUY_COUNT)
        self.assertEqual(
            f'[NEMO]{TEST_CODE} buy stock ( price : {BUY_PRICE} ) * ( count : {BUY_COUNT})\n',
            captured_output.getvalue()
        )

    def test_sell(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.nemo_driver.sell(TEST_CODE, SELL_PRICE, SELL_COUNT)
        self.assertEqual(
            f'[NEMO]{TEST_CODE} sell stock ( price : {SELL_PRICE} ) * ( count : {SELL_COUNT})\n',
            captured_output.getvalue()
        )

    @patch.object(NemoAPI, 'get_market_price', return_value=BUY_PRICE)
    def test_get_price(self, mock):
        current_price = self.nemo_driver.get_price(TEST_CODE)
        self.assertEqual(BUY_PRICE, current_price)

    @patch.object(NemoAPI, 'get_market_price', return_value=SELL_PRICE)
    def test_get_price_after_3(self, mock):
        current_price = self.nemo_driver.get_price(TEST_CODE, 3)
        self.assertEqual(SELL_PRICE, current_price)
