from selenium.webdriver.support.wait import WebDriverWait
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


from calculator.utils.logger import Logger

log = Logger.get_logger()


class Base:
    def __int__(self):
        log.info("initiating driver")
        self.driver = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
        # 打开url
        self.driver.get("https://csmoodle.ucd.ie/moodle/")
        self.driver.maximize_window()

    def base_find_element(self, loc, timeout=30, poll_freq=0.5):
        # 查找元素
        # 不传参数默认30的timeout 和 0.5的freq
        # *loc: 解包元组中的元素
        log.info("finding element: {}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_freq).until(
            lambda x: x.find_element(*loc))

    def base_click(self, loc):
        # 点击
        log.info("clicking element: {}".format(loc))
        self.base_find_element(loc).click()

    def base_input(self, loc, input):
        # 输入
        log.info("clear element: {}".format(loc))
        self.base_find_element(loc).clear()
        log.info("inputting '{}' into element: {}".format(input, loc))
        self.base_find_element(loc).send_keys(input)

    def base_get_info(self, loc):
        # 获取错误信息
        log.info("finding info from element: {}".format(loc))
        return self.base_find_element(loc).text

    def base_screen_shot(self):
        # 截图
        log.info("making screen shot")
        self.driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
