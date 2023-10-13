import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from ucd_login import page
from ucd_login.base.base import Base


class PageLogin(Base):
    # 页面操作类，封装页面操作的方法

    def page_input_username(self, username):
        # 输入用户名
        self.base_input(page.LOGIN_USERNAME, username)

    def page_input_pwd(self, pwd):
        # 输入密码
        self.base_input(page.LOGIN_PWD, pwd)

    def page_click_login(self):
        # 点击登录
        self.base_click(page.LOGIN_BTN)

    def page_get_error_info(self):
        # 获取异常信息
        return self.base_get_info(page.LOGIN_INFO)

    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login()
