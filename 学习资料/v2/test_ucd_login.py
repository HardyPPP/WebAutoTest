import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        # 初始化
        # 获取浏览器驱动对象
        cls.driver = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
        # 打开url
        cls.driver.get("https://csmoodle.ucd.ie/moodle/")
        cls.driver.maximize_window()
        # 隐式等待
        # self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # teardown
        # 关闭浏览器
        sleep(2)
        cls.driver.quit()

    def test_login_wrong_pwd(self):
        # 判断密码错误
        driver = self.driver
        # 点击登录链接
        # driver.find_element(By.ID, "#login")
        # 输入正确的用户名
        username = driver.find_element(By.CSS_SELECTOR, '#username')
        username.clear()
        username.send_keys("20205766")
        # 输入错误的密码
        pwd = driver.find_element(By.CSS_SELECTOR, '#password')
        pwd.clear()
        pwd.send_keys("1234567")
        # 输入验证码
        # driver.find_element(By.CSS_SELECTOR, '#verify_code').send_keys("")
        # 点击登录
        driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-login"]').click()
        # 获取登录后的信息
        result = driver.find_element(By.CSS_SELECTOR, 'p[class="form-element form-error"]').text
        # 定义预期结果
        expect = "The password you entered was incorrect."
        # 断言
        try:
            self.assertEqual(result, expect)
        except AssertionError:
            driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
            # 截图
            raise

    def test_login_username_not_exist(self):
        # 判断密码错误
        driver = self.driver
        # 点击登录链接
        # driver.find_element(By.ID, "#login")
        # 输入错误的用户名
        username = driver.find_element(By.CSS_SELECTOR, '#username')
        username.clear()
        username.send_keys("2222222")
        # 输入错误的密码
        pwd = driver.find_element(By.CSS_SELECTOR, '#password')
        pwd.clear()
        pwd.send_keys("1234567")
        # 输入验证码
        # driver.find_element(By.CSS_SELECTOR, '#verify_code').send_keys("")
        # 点击登录
        driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-login"]').click()
        # 获取登录后的信息
        result = driver.find_element(By.CSS_SELECTOR, 'p[class="form-element form-error"]').text
        # 定义预期结果
        expect = "The username you entered cannot be identified."
        # 断言
        try:
            self.assertEqual(result, expect)
        except AssertionError:
            driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
            # 截图
            raise
