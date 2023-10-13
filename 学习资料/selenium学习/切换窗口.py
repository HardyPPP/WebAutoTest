from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
wd.implicitly_wait(1)
wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, "a")
link.click()

# mainWindow变量保存当前窗口的句柄
mainWindow = wd.current_window_handle

for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
# 上面代码的用意就是：
#
# 我们依次获取 wd.window_handles 里面的所有 句柄 对象， 并且调用 wd.switch_to.window(handle) 方法，切入到每个窗口，
#
# 然后检查里面该窗口对象的属性（可以是标题栏，地址栏），判断是不是我们要操作的那个窗口，如果是，就跳出循环。

print(wd.title)

wd.find_element(By.ID, 'sb_form_q').send_keys('baidu\n')

# 通过前面保存的老窗口的句柄，自己切换到老窗口
wd.switch_to.window(mainWindow)

btn = wd.find_element(By.ID, 'outerbutton')

for i in range(0, 10):
    btn.click()

input()
