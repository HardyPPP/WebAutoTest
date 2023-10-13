from selenium.webdriver.common.by import By

DRIVER_LOC = r'd:\chromedriver.exe'
URL = "http://cal.apple886.com/"

"""以下为计算器页面配置数据"""
CAL_NUM = By.CSS_SELECTOR, '#simple'
CAL_EQ = By.CSS_SELECTOR, '#simpleEqual'
CAL_PLUS_BTN = By.CSS_SELECTOR, '#simpleAdd'
CAL_RESULT = By.CSS_SELECTOR, '#resultIpt'
CAL_CLEAR = By.CSS_SELECTOR, '#simpleClearAllBtn'