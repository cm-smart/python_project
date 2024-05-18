import urllib.request
# https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
url = 'https://movie.douban.com/j/search_subjects?'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
data = {
    'type':'movie',
    'tag':'热门',
    'page_limit':10,
    'page_start':0
}
new_data = urllib.parse.urlencode(data)
url = url + new_data
print(url)
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 数据下载到本地
fp = open(file='douban.json',mode='w',encoding='utf-8')
fp.write(content)