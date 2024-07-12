import sys
import io

import unittest
from unittest import TestCase
from unittest.mock import Mock, patch

from nemo_driver import NemoDriver

ID = 'SAMSUNG'
PWD = 'tka123tjd!'

STOCK_CODE = 'SAM'
PRICE = 80000
COUNT = 100


class TestNemoDriver(TestCase):
    def setUp(self):
        self.nemo_driver = NemoDriver()
        self.output = io.StringIO()

    def test_nemo_login(self):
        sys.stdout = self.output
        self.nemo_driver.login(ID, PWD)
        self.assertEqual(self.output.getvalue(), '[NEMO]' + ID + ' login GOOD\n')

    def test_nemo_buy(self):
        sys.stdout = self.output
        self.nemo_driver.buy(STOCK_CODE, PRICE, COUNT)
        self.assertEqual(self.output.getvalue(),
                         '[NEMO]' + STOCK_CODE + ' buy stock ( price : ' + str(PRICE) + ' ) * ( count : ' + str(
                             COUNT) + ')\n')

    def test_nemo_sell(self):
        sys.stdout = self.output
        self.nemo_driver.sell(STOCK_CODE, PRICE, COUNT)
        self.assertEqual(self.output.getvalue(),
                         '[NEMO]' + STOCK_CODE + ' sell stock ( price : ' + str(PRICE) + ' ) * ( count : ' + str(
                             COUNT) + ')\n')

    @patch.object(NemoDriver, 'get_price')
    def test_nemo_get_price(self, mk):
        mk.return_value = 5532
        self.assertEqual(self.nemo_driver.get_price(STOCK_CODE, 1), 5532)


if __name__ == '__main__':
    unittest.main()
