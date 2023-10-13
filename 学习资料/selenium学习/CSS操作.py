from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

elements = wd.find_elements(By.CSS_SELECTOR, '#container > div')
# 找id为container的直接子元素div集合

print(1)
for element in elements:
    print('--------------')
    print(element.get_attribute('outerHTML'))

elements = wd.find_elements(By.CSS_SELECTOR, '#layer1 > #inner11 > span')
# 使用大于号链接：必须是直接子元素

print(2)
for element in elements:
    print('--------------')
    print(element.get_attribute('outerHTML'))

elements = wd.find_elements(By.CSS_SELECTOR, '#layer1 span')
# 是有空格链接：只要包含就行

print(3)
for element in elements:
    print('--------------')
    print(element.get_attribute('outerHTML'))

elements = wd.find_elements(By.CSS_SELECTOR, '.plant span')
# 是有空格链接：只要包含就行

print(4)
for element in elements:
    print('--------------')
    print(element.get_attribute('outerHTML'))

elements = wd.find_elements(By.CSS_SELECTOR, 'a[href="http://www.miitbeian.gov.cn"]')
# 属性选择 a是tag，后面可以不加等号，会直接找有这个属性的元素
# CSS 还可以选择 属性值 包含 某个字符串 的元素
#
# 比如， 要选择a节点，里面的href属性包含了 miitbeian 字符串，就可以这样写
#
# a[href*="miitbeian"]
#
# 还可以 选择 属性值 以某个字符串 开头 的元素
#
# 比如， 要选择a节点，里面的href属性以 http 开头 ，就可以这样写
#
# a[href^="http"]
#
# 还可以 选择 属性值 以某个字符串 结尾 的元素
#
# 比如， 要选择a节点，里面的href属性以 gov.cn 结尾 ，就可以这样写
#
# a[href$="gov.cn"]
# 如果一个元素具有多个属性
#
# <div class="misc" ctype="gun">沙漠之鹰</div>
# CSS 选择器 可以指定 选择的元素要 同时具有多个属性的限制，像这样 div[class=misc][ctype=gun]
# 属性之间不能加空格，不然就变成父元素->子元素了
print(5)
for element in elements:
    print('--------------')
    print(element.get_attribute('outerHTML'))




