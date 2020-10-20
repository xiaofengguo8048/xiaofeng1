import unittest
import pytest
from payfunc import *

class PayTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_pt1(self):
        self.assertEqual(paytt(1), 'success', msg='error')

    def test_pt2(self):
        self.assertEqual(paytt(0), 'fail', msg='error')

    def test_pt3(self):
        self.assertEqual(paytt(2), 'processing', msg='error')

if __name__ == '__main__':
    unittest.main()
