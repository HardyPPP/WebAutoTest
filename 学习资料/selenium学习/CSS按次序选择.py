from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)')
# 找到父元素第二个子元素且tag为span的

print(1)
for element in elements:
    print('--------------')
    print(element.get_attribute('outerHTML'))

elements = wd.find_elements(By.CSS_SELECTOR, '#t1 :nth-child(2)')
# 找到父元素id为t1的第二个子元素

print(2)
for element in elements:
    print('--------------')
    print(element.get_attribute('outerHTML'))

elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-of-type(1)')
# 找第一个span类型的子元素

print(3)
for element in elements:
    print('--------------')
    print(element.get_attribute('outerHTML'))

