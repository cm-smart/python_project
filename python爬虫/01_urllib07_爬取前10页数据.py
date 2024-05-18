import urllib.request

def create_request(page):
    url = 'https://movie.douban.com/j/search_subjects?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    data = {
        'type': 'movie',
        'tag': '热门',
        'page_limit': 10,
        'page_start': page
    }
    new_data = urllib.parse.urlencode(data)
    new_url = url + new_data
    print(new_url)
    return urllib.request.Request(url=new_url,headers=headers)

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    return content

def down_load(page,content):
    with open(file='douban_' + str(page) + '.json',mode='w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start = int(input("请输入开始页："))
    end = int(input("请输入结束页："))
    for i in range(start,end+1):
        request = create_request(i)
        content = get_content(request)
        down_load(i,content)



