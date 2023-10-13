import unittest


class Test05(unittest.TestCase):
    def test01(self):
        flag = True
        # 断言是否为true
        self.assertTrue(flag)

    def test02(self):
        flag = False
        # 断言是否为False
        self.assertFalse(flag)

    def test03(self):
        flag = False
        # 断言是否相等
        self.assertEqual("hello", "hello")
    #   self.assertNotEqual("hello", "hello")
    #   断言不等

    def test04(self):
        flag = False
        # 断言是否后面的字符串是否包含前面字符串(前是后的子串
        self.assertIn("hello", "hello1231231")

    def test05(self):
        flag = None
        # 断言是否为None
        self.assertIsNone(flag)
        # self.assertIsNotNone(flag)
        # 断言不是None