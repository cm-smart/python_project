import urllib.request

url = 'https://www.baidu.com/'

name = urllib.parse.quote('华友钴业')
print(name)

data = {
    'wd':'周杰伦',
    'sex':'男'
}
a = urllib.parse.urlencode(data)
print(a)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)