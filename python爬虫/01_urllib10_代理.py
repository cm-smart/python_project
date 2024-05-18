# 突破自身ip访问限制，访问国外网站
# 访问一些单位或团体内部资源
# 提高访问速度
# 隐藏真实ip

import urllib.request
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request)
proxies = {
    'http':'202.101.213.67:20419'
}
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)
