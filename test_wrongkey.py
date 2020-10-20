import unittest
import pytest
from payfunc import *

class Test:
    def test_input_one(self):
        assert paytt(1) == 'success'
# class Test_wrongkey:
#     def test_input_equals_one(self):
#         print('test1')
#         assert paytt(1) == 'success'
    #
    # def test_a2(self):
    #     print('test2')
    #     assert 2 == 2
    #
    # def test_a3(self):
    #     print('test3')
    #     assert 3 == 2


if __name__ == '__main__':
    pytest.main()
