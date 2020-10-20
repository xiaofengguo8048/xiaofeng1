import unittest


from payfunc import *

class PayTest(unittest.TestCase):


    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_pt1(self):
        self.assertEqual(paytt(1), '支付成功', msg='error')

    def test_pt2(self):
        self.assertEqual(paytt(0), '支付失败', msg='error')

    def test_pt3(self):
        self.assertEqual(paytt(2), '处理', msg='error')
    def test4(self):
        prin(1)

if __name__ == '__main__':
    unittest.main()
