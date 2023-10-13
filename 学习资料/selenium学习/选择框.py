from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
wd.implicitly_wait(1)
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# radio
# 获取当前选中的元素
element = wd.find_element(By.CSS_SELECTOR,
                          '#s_radio input[name="teacher"]:checked')
print('当前选中的是: ' + element.get_attribute('value'))

# 点选 小雷老师
wd.find_element(By.CSS_SELECTOR,
                '#s_radio input[value="小雷老师"]').click()

# checkbox
# 先把 已经选中的选项全部点击一下
elements = wd.find_elements(By.CSS_SELECTOR,
                            '#s_checkbox input[name="teacher"]:checked')

for element in elements:
    element.click()

# 再点击 小雷老师
wd.find_element(By.CSS_SELECTOR,
                "#s_checkbox input[value='小雷老师']").click()

# select
# 导入Select类
from selenium.webdriver.support.ui import Select

# 创建Select对象
select = Select(wd.find_element(By.ID, "ss_single"))

# 通过 Select 对象选中小雷老师
select.select_by_visible_text("小雷老师")

# 导入Select类
from selenium.webdriver.support.ui import Select

# 创建Select对象
select = Select(wd.find_element(By.ID, "ss_multi"))

# 清除所有 已经选中 的选项
select.deselect_all()

# 选择小雷老师 和 小凯老师
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小江老师")

input()
