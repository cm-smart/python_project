# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# print(1)
# path = r'C:\Users\Lenovo\AppData\Local\Google\Chrome\Application\chrome.exe'
# options.binary_location = path
# print(2)
# browser = webdriver.Chrome(options=options)
#
#
# url = 'http://www.baidu.com'
# browser.get(url)
# # 保存当前截屏
# browser.save_screenshot("baidu.png")
#
# browser.quit()
# 这个没有做好，不能执行
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')     # path是你自己的chrome浏览器的文件路径
    path = r'C:\Users\Lenovo\AppData\Local\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(options=chrome_options)
    return browser

browser = share_browser()
url = 'https://www.baidu.com'
browser.get(url)


