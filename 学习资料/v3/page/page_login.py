import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class PageLogin:
    # 页面操作类，封装页面操作的方法
    driver = None

    def __int__(self):
        # 初始化
        # 获取浏览器驱动对象
        self.driver = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
        # 打开url
        self.driver.get("https://csmoodle.ucd.ie/moodle/")
        self.driver.maximize_window()
        # 隐式等待
        # self.driver.implicitly_wait(10)

    def page_input_username(self, username):
        # 输入用户名
        self.driver.find_element(By.CSS_SELECTOR, '#username').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)

    def page_input_pwd(self, pwd):
        # 输入密码
        self.driver.find_element(By.CSS_SELECTOR, '#password').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(pwd)

    def page_click_login(self):
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-login"]').click()

    def page_get_error_info(self):
        # 获取异常信息
        return self.driver.find_element(By.CSS_SELECTOR, 'p[class="form-element form-error"]').text

    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login()
