import unittest
from parameterized import parameterized


def get_data():
    return [(1, 2, 3), (3, 0, 3), (2, 1, 3), (2, -1, 1)]


def add(x, y):
    return x + y


class Test01(unittest.TestCase):
    @parameterized.expand([1, 2, 3])
    def test01(self, num):
        print("num: ", num)

    @parameterized.expand([(1, 2, 3), (3, 0, 3), (2, 1, 3), (2, -1, 1)])
    def test02(self, a, b, result):
        print("{} + {} = {} ".format(a, b, result))

    @parameterized.expand(get_data())
    def test03(self, a, b, expresult):
        result = add(a, b)
        assert result == expresult
        print("{} + {} = {} ".format(a, b, expresult))
