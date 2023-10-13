import unittest

VERSION = 35

class TestSkip(unittest.TestCase):
    @unittest.skip("功能未实现")
    def test01(self):
        """
        功能未完成
        :return:
        """
        print('test01')

    @unittest.skipIf(VERSION > 25, "版本已更新，跳过")
    def test02(self):
        pass
