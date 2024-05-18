import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
data = {
    'kw':'spider'
}
new_data = urllib.parse.urlencode(data).encode('utf-8')
# post请求，参数必须是字节
request = urllib.request.Request(url=url,data=new_data,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

# post请求方式参数必须编码
# 编码之后必须encode方法 将字符串转为二进制
# decode 将二进制转为字符串