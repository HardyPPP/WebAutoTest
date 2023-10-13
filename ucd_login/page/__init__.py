from selenium.webdriver.common.by import By

"""以下为登录页面配置数据"""
LOGIN_USERNAME = By.CSS_SELECTOR, '#username'
LOGIN_PWD = By.CSS_SELECTOR, '#password'
LOGIN_BTN = By.CSS_SELECTOR, 'button[class="btn btn-login"]'
LOGIN_INFO = By.CSS_SELECTOR, 'p[class="form-element form-error"]'
