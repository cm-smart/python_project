from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chromeService = ChromeService(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=chromeService)

url = 'http://www.baidu.com'
browser.get(url)
#
# element = browser.find_element(By.ID,'su')
# # 获取属性值
# class_name = element.get_attribute('class')
# print(class_name)
# # 获取标签名
# tag_name = element.tag_name
# print(tag_name)
# # 获取元素文本 <button>按钮</button>
# text = element.text
# print(text)
# link = browser.find_element(By.LINK_TEXT,'新闻')
# print(link.text)

# 浏览器自动化
import time
time.sleep(2)

# 获取文本框对象
input = browser.find_element(By.ID,'kw')
# 在文本框中输入周杰伦
input.send_keys('周杰伦')
time.sleep(2)
# 获取百度一下按钮
button = browser.find_element(By.ID,'su')
# 点击按钮
button.click()
time.sleep(2)

#滑倒底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)

# 获取下一页的按钮
button_next = browser.find_element(By.XPATH,'//div[@class="page-inner_2jZi2"]/a[@class="n"]')
print(button_next)
button_next.click()

time.sleep(2)

# 回到上一页
browser.back()
time.sleep(2)
# 向前
browser.forward()

time.sleep(3)

# 退出
browser.quit()



