from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
elements = wd.find_elements(By.CLASS_NAME, 'animal')
# find_elements找不到返回空列表
# find_element找不到抛出异常

# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)