import urllib.request
import jsonpath
import json

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1716012395200_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Bx-V':'2.5.11',
    'Cookie':'t=dad95e1fe2cecea628e2d3357cea20f5; cookie2=13328cda9ba8fb88113255456d80c214; v=0; _tb_token_=19e5be54a179; cna=F9vOHop5QDgCASRxHmiVtBib; xlly_s=1; isg=BG5ut2wihBExyPB6Jb8uDB5wv8QwbzJpVck1hJg3rXEsew7VAP9TeUt1M-eXpiqB',
    'Priority':'u=1, i',
    'Referer':'https://dianying.taobao.com/',
    'Sec-Ch-Ua':'"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':"Windows",
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
print(content.split('(')[1].split(')')[0])
with open(file='taopiaopiao.json',mode='w',encoding='utf-8') as fp:
    fp.write(content.split('(')[1].split(')')[0])


obj = json.load(open(file='taopiaopiao.json',mode='r',encoding='utf-8'))
regionName_list = jsonpath.jsonpath(obj,'$..regionName')
print(regionName_list)
print(len(regionName_list))