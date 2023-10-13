import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from calculator.base.get_driver import GetDriver
from calculator.page.page_calculator import PageCalculator
from parameterized import parameterized

from calculator.utils.read_json import read_json


class TestCalculator(unittest.TestCase):
    # 测试类
    calculator = None

    @classmethod
    def setUpClass(cls):
        # 获取登录页面对象
        cls.calculator = PageCalculator()
        cls.calculator.__int__()

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        # 关闭驱动对象
        cls.calculator.driver.quit()

    @parameterized.expand(read_json())
    def test_add(self, a, b, exp_result):
        self.calculator.page_calculate(a, b)
        result = self.calculator.page_get_result()
        try:
            self.assertEqual(result, str(exp_result))
        except AssertionError:
            # self.calculator.driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
            # # 截图
            raise

    # def test_login(self, username, pwd, exp_result):
    #     # 调用测试登录方法
    #     self.calculator.page_login(username, pwd)
    #     # 获取登陆后的信息
    #     result = self.calculator.page_get_error_info()
    #     # 断言
    #     try:
    #         self.assertEqual(result, exp_result)
    #     except AssertionError:
    #         self.calculator.driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
    #         # 截图
    #         raise
