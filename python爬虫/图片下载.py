# 爬取页面上的所有图片
import urllib.request
from lxml import etree

url = 'https://sc.chinaz.com/tupian/shaofutupian.html'

response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)

# with open(file='shaofutupian.html',mode='w',encoding='utf-8') as ft:
#     ft.write(content)

# 解析数据
tree = etree.HTML(content)
data_list_src = tree.xpath('//div[@class="item"]/img/@data-original')
data_list_alt = tree.xpath('//div[@class="item"]/img/@alt')
print(len(data_list_src))
print(len(data_list_alt))

for i in range(1,len(data_list_src)):
    print(data_list_alt[i],data_list_src[i])

# 图片下载
# img_url = 'https://scpic2.chinaz.net/files/default/imgs/2023-08-29/573d9982b5f87804_s.jpg'
#
# urllib.request.urlretrieve(url=img_url,filename='1.jpg')


