import unittest


def add(x, y):
    return x + y


class Test02(unittest.TestCase):
    def test_add(self):
        result = add(1, 4)
        print("结果为 ", result)

    def test_add2(self):
        result = add(1, 12)
        print("结果为 ", result)


