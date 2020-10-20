import pytest

class Test_wrongkey:
    def test_a1(self):
        print('test1')
        assert 1 == 1

    def test_a2(self):
        print('test2')
        assert 2 == 2

    def test_a3(self):
        print('test3')
        assert 3 == 2


if __name__ == '__main__':
    pytest.main()
