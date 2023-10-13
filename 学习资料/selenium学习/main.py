from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))

wd.implicitly_wait(10)
# 隐式等待，找不到元素不立刻抛出异常，而是每半秒请求一次，直到超时（参数是超时的时间）

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.byhy.net/_files/stock1.html')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
try:
    element = wd.find_element(By.ID, 'kw')
    # 通过该 WebElement对象，就可以对页面元素进行操作了
    # 比如输入字符串到 这个 输入框里

    element.send_keys('通讯')

    print(element.get_attribute('value'))
    # 获取输入框的输入值

    element_btn = wd.find_element(By.ID, 'go')
    # 按钮操作
    element_btn.click()

    # 返回页面 ID为1 的元素
    element_result = wd.find_element(By.ID, '1')

    print(element_result.text)
    print("Class:")
    print(element_result.get_attribute('class'))
    # 获取该元素的class属性
    print("outerHTML:")
    print(element_result.get_attribute('outerHTML'))
    print("innerHTML:")
    print(element_result.get_attribute('innerHTML'))

    element.clear()  # 清除输入框已有的字符串
    element.send_keys('科技')  # 输入新字符串
    element_btn.click()

    element_result = wd.find_element(By.ID, '1')
    print(element_result.text)
    # 通过WebElement对象的
    # text
    # 属性，可以获取元素
    # 展示在界面上的
    # 文本内容。
    #
    # 但是，有时候，元素的文本内容没有展示在界面上，或者没有完全完全展示在界面上。 这时，用WebElement对象的text属性，获取文本内容，就会有问题。
    #
    #
    # 出现这种情况，可以尝试使用
    # element.get_attribute('innerText') ，或者
    # element.get_attribute('textContent')
    print(element_result.get_attribute('class'))

    input('等待回车键结束程序')
    # 程序运行完会自动关闭浏览器，就是很多人说的闪退
    # 这里加入等待用户输入，防止闪退
    # 结束
    wd.quit()
except NoSuchElementException:
    print("元素不存在")


