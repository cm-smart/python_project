from bs4 import BeautifulSoup
import urllib.request

url = 'https://tieba.baidu.com/p/7882177660?pn='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}


def create_request(page):
    newUrl = url + str(page)
    print(newUrl)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode()
    return content

if __name__ == '__main__':
    request = create_request(1)
    html = get_content(request)
    soup = BeautifulSoup(html, 'lxml')
    comments = soup.select('.d_post_content')
    for i in range(0,len(comments)):
        strs = comments[i].strings
        temp = ''
        for text in strs:
            temp = temp + text
        print(temp)