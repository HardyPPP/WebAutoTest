from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from calculator import page


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome(service=Service(page.DRIVER_LOC))
            # 打开url
            cls.driver.get(page.URL)
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


if __name__ == "__main__":
    print(GetDriver.get_driver())
