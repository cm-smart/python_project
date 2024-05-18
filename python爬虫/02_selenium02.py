from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService

service = ChromService(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)
url = 'https://www.baidu.com'

browser.get(url)

print("当前页面标题：",browser.title)

# 退出浏览器
browser.quit()

