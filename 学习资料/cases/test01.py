import unittest


def add(x, y):
    return x + y


class Test01(unittest.TestCase):
    def test_add(self):
        result = add(1, 1)
        print("结果为 ", result)

    def test_add2(self):
        result = add(1, 3)
        print("结果为 ", result)
