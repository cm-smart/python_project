import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

print("response类型：",type(response))

# 读取5个字节
# content = response.read(5)
# 读取一行记录
# content = response.readline()
# 一行一行读取全部数据
# content = response.readlines()
# code = response.getcode()
# print(code)

print(response.url)
print(response.getheaders())

# 返回字节形式的二进制
# content = response.read().decode('utf-8')
#
# print(content)