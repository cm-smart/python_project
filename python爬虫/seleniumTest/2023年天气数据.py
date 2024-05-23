import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def create_browser():
    chromeService = ChromeService(executable_path='../chromedriver.exe')
    browser = webdriver.Chrome(service=chromeService)

    url = 'http://www.weather.com.cn/weather40d/101010100.shtml'
    browser.get(url)
    return browser

# 点击月份触发事件
def click_li(browser):

    div1 = browser.find_element(By.XPATH, '//div[@class="zong"]')
    div1.click()
    li_list = browser.find_elements(By.XPATH, '//div[@class="w_nian"]/ul[1]/li')

    for li in li_list:
        li.click()
        # 这边必须要等待，因为浏览器执行速度没有代码快，有可能导致页面上的数据爬取不到
        time.sleep(2)
        date_list = browser.find_elements(By.XPATH, '//table[@id="table"]//span[contains(@class,"nowday")]')
        max_wd_list = browser.find_elements(By.XPATH, '//table[@id="table"]//div[@class="w_xian"]//span[@class="max"]')
        min_wd_list = browser.find_elements(By.XPATH, '//table[@id="table"]//div[@class="w_xian"]//span[@class="min"]')
        jsgl_list = browser.find_elements(By.XPATH, '//table[@id="table"]//div[@class="w_xian"]//span[@class="tubiao"]')
        str_month = li.text.split("月")[0]
        month = resolve(str_month)

        resolve_click_month(month,date_list,max_wd_list,min_wd_list,jsgl_list)

# 判断str在数组date_array是否存在
def isExist(str,date_array):
    for temp in date_array:
        if(str == temp):
            return True
        else:
            return False
# 格式月份
def resolve(month):
    temp = int(month.split('月')[0])
    if temp < 10:
        return '0' + str(temp)
    else:
        return str(temp)
# 解析数据
def resolve_click_month(month,date_list,max_wd_list,min_wd_list,jsgl_list):
    flag = False
    date_array = []
    for i in range(0, len(date_list)):
        date = date_list[i].text
        if date == '01':
           flag = True
        if flag:
            if isExist(date,date_array):
                break
            date_array.insert(i, date)
            date_str = '2023-' + month + '-' + date
            if date != '':
                line = date_str + '\t' + max_wd_list[i].text + '\t' + min_wd_list[i].text + '\t' + jsgl_list[i].text
                print(line)
                with open(file='2023天气数据.txt', mode='a+', encoding='utf-8') as df:
                    df.write(line + '\n')

if __name__ == '__main__':
    browser = create_browser()
    click_li(browser)

