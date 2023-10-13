from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
wd.implicitly_wait(1)
wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')
# 先根据name属性值 'innerFrame'，切换到iframe中
# wd.switch_to.frame('innerFrame')
# 或者 wd.switch_to.frame(wd.find_element(By.TAG_NAME, "iframe"))
# 或者
wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, 'iframe[src="sample1.html"]'))
# 根据 class name 选择元素，返回的是 一个列表
elements = wd.find_elements(By.CLASS_NAME, 'plant')

for element in elements:
    print(element.text)

# 切换回 最外部的 HTML 中
wd.switch_to.default_content()

# 然后再 选择操作 外部的 HTML 中 的元素
btn = wd.find_element(By.ID, 'outerbutton')

btn.click()
btn.click()
btn.click()

text = wd.find_elements(By.CSS_SELECTOR, '#add li')
for t in text:
    print(t.text)

wd.quit()