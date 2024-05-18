import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chromeService = ChromeService(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=chromeService)

url = 'http://www.baidu.com'
browser.get(url)

# 元素定位
# 根据id获取元素
# element = browser.find_element(By.ID,'su')
# 根据name获取元素
# element = browser.find_element(By.NAME,'wd')
# 根据class属性获取元素
# element = browser.find_element(By.CLASS_NAME,'s_ipt')
# 根据css语法获取元素
# element = browser.find_element(By.CSS_SELECTOR,'#su')
# 根据xpath语法获取元素
element = browser.find_element(By.XPATH,'//input[@id="su"]')
# By.TAG_NAME
# By.LINK_TEXT
print(element)

time.sleep(2)

browser.quit()


