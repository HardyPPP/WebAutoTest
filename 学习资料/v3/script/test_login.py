import time
import unittest
from time import sleep

from 学习资料.v3.page.page_login import PageLogin
from parameterized import parameterized


def get_data():
    return [('20205766', '1234567', 'The password you entered was incorrect.'),
            ('222222', '1234567', 'The username you entered cannot be identified.')]


class TestLogin(unittest.TestCase):
    # 测试类
    login = None

    @classmethod
    def setUpClass(cls):
        # 获取登录页面对象
        cls.login = PageLogin()
        cls.login.__int__()

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        # 关闭驱动对象
        cls.login.driver.quit()

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, exp_result):
        # 调用测试登录方法
        self.login.page_login(username, pwd)
        # 获取登陆后的信息
        result = self.login.page_get_error_info()
        # 断言
        try:
            self.assertEqual(result, exp_result)
        except AssertionError:
            self.login.driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
            # 截图
            raise
