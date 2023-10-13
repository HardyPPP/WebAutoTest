import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from calculator import page
from calculator.base.base import Base


class PageCalculator(Base):
    # 页面操作类，封装页面操作的方法

    def page_click_add(self):
        # 点击+
        self.base_click(page.CAL_PLUS_BTN)

    def page_click_num(self, num):
        for n in str(num):
            # 拆开数字挨个点击
            loc = By.CSS_SELECTOR, "#simple{}".format(n)
            # 点击数字
            self.base_click(loc)

    def page_click_eq(self):
        # 点击=
        self.base_click(page.CAL_EQ)

    def page_click_clear(self):
        # 点击清屏
        self.base_click(page.CAL_CLEAR)

    def page_get_result(self):
        # 获取结果
        return self.base_get_info(page.CAL_RESULT)

    def page_calculate(self, a, b):
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()

