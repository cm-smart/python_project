import urllib.request
import urllib.error

url = 'http://www.baidu.com/1'
try:
    response = urllib.request.urlopen(url=url)
    content = response.read().decode('utf-8')
except urllib.error.HTTPError:
    print('发生httpError')
except urllib.error.URLError:
    print('发生urlError')
