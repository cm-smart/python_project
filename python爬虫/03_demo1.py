import urllib.request
from lxml import etree

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


def resolve(content):
    tree = etree.HTML(content)
    comments = tree.xpath('//div[@class="d_post_content j_d_post_content "]')
    users = tree.xpath('//div[@class="d_author"]//a[@class="p_author_name j_user_card"]')
    sorts = tree.xpath('(//div[@class="post-tail-wrap"]/span[last()-1])')
    times = tree.xpath('(//div[@class="post-tail-wrap"]/span[last()])')
    print(comments)
    print(users)
    print(times)
    print(len(comments))
    print(len(users))
    print(len(times))

    for i in range(0, len(comments)):
        comment = comments[i]
        str = comment.text.strip()
        if str == '':
            print(1)
            print(comment.getchildren.text)
        print(str)
        # print(type(users[i]))
        # print(users[i], sorts[i],comments[i], times[i])


if __name__ == '__main__':
    page = int(input("请输入需要爬取多少页："))
    for i in range(0,page):
        request = create_request(i+1)
        content = get_content(request)
        print(content)
        resolve(content)
