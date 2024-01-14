import os
import random
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

headers_list = [
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
    }, {
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
    }, {
        'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    }, {
        'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    }, {
        'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
]

chapter = int(input("选择章节："))
chapterPage = int(input("选择起始页页码（从0开始）："))

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
wd.implicitly_wait(10)
wd.get('https://manhuapica.com/plogin/')

print("正在登录")
phone = wd.find_element(By.XPATH, '//*[@id="email1"]')
password = wd.find_element(By.XPATH, '//*[@id="password1"]')
phone.send_keys("18722396825")
password.send_keys("hardy2001")
btn = wd.find_element(By.XPATH, '//*[@id="appCapsule"]/div[1]/div/div[2]/formsss/button')
btn.click()
# 登录
print("已登录")
sleep(10)

wd.find_element(By.XPATH, '//*[@id="homecontentbox"]/div/div/div[2]/div/label[2]').click()
print("已点击开屏广告")
sleep(1)
accept = wd.find_element(By.XPATH, '//*[@id="cookies-box"]/a')
# 接受cookie
accept.click()
print("已接受cookie")

j = chapter
i = chapterPage

wd.get(
    'https://manhuapica.com/pchapter/?cid=5c8fc916459fef312807decb&chapter={}&chapterPage=1&maxchapter=120'.format(j))
print("已跳转到目标页面")
# 跳转到目标页面
sleep(15)

# modal = wd.find_element(By.XPATH, '//*[@id="changeModal"]/div/div/div[3]/div/a[2]')
#
# modal.click()

# accept = wd.find_element(By.XPATH, '//*[@id="cookies-box"]/a')
# if accept is not None:
#     accept.click()
try:
    element0 = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="changeModal"]/div/div'
                                                                                 '/div[3]/div/a[2]')))
    wd.find_element(By.XPATH, '//*[@id="changeModal"]/div/div/div[3]/div/a[2]').click()
    print("已刷新页面")
    sleep(10)
except ElementNotInteractableException:
    print("元素不可交互")

# os.path.join()拼接路径
parent_directory = "../img"
new_subdirectory = "{}".format(j)
new_full_path = os.path.join(parent_directory, new_subdirectory)
if not os.path.exists(new_full_path):
    # 创建子目录
    os.makedirs(new_full_path)

while j < 120:
    element = wd.find_element(By.XPATH, '//*[@id="appCapsule"]/div[1]/div[3]')
    child = element.find_elements(By.XPATH, './*')
    loadCount = 0
    # 获取子元素
    print(len(child))
    if i != 0:
        scroll_distance = 400  # 设置滚动的距离
        wd.execute_script(f"window.scrollBy(0, {scroll_distance * i});")
    while i < len(child) - 3:
        element = wd.find_element(By.XPATH, '//*[@id="appCapsule"]/div[1]/div[3]')
        child = element.find_elements(By.XPATH, './*')
        element_class = child[i].get_attribute("class")
        print("i = {}".format(i))

        if "lazyloaded" in element_class and child[i].tag_name == "img":
            loadCount = 0
            print("已加载")
            scroll_distance = 1400  # 设置滚动的距离
            wd.execute_script(f"window.scrollBy(0, {scroll_distance});")
            img_src = child[i].get_attribute("src")

            headers = random.choice(headers_list)
            # 使用HTTP请求下载img
            while True:  # 循环
                try:
                    # r = eval(expression)
                    response = requests.get(img_src, headers=headers, timeout=50)
                    print("下载中")
                    local_filename = "../img/{}/{}.png".format(j, i)
                    # 保存img到本地
                    with open(local_filename, "wb") as f:
                        f.write(response.content)
                    print("下载完成")
                except (requests.exceptions.SSLError, requests.exceptions.ConnectionError) as e:
                    if 'bad handshake' in str(e) or '10054' in str(e):  # 2种异常
                        print("下载失败，正在重试")
                        continue  # 继续发请求
                    else:
                        raise Exception(e)  # 其他异常
                break  # 无异常就跳出

            # response = requests.get(img_src, headers=headers)

            i = i + 1
        elif "lazyload" in element_class:
            # wd.execute_script("arguments[0].scrollIntoView(true);", child[0])
            #     页面滚动到未加载的图片
            sleep(1)
            scroll_distance = 300  # 设置滚动的距离
            wd.execute_script(f"window.scrollBy(0, {scroll_distance});")
            loadCount = loadCount + 1
            if loadCount > 10:
                loadCount = 0
                scroll_distance = -2000  # 设置滚动的距离
                wd.execute_script(f"window.scrollBy(0, {scroll_distance});")
            print("加载中")
            sleep(2)
        else:
            loadCount = 0
            i = i + 1
    sleep(2)
    i = 0
    j = j + 1

    # os.path.join()拼接路径
    parent_directory = "../img"
    new_subdirectory = "{}".format(j)
    new_full_path = os.path.join(parent_directory, new_subdirectory)

    if not os.path.exists(new_full_path):
        # 创建子目录
        os.makedirs(new_full_path)
    wd.get(
        'https://manhuapica.com/pchapter/?cid=5c8fc916459fef312807decb&chapter={}&chapterPage=1&maxchapter=120'.format(
            j))
    sleep(2)
