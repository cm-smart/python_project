import urllib.request

url = 'http://www.baidu.com'
# 下载
urllib.request.urlretrieve(url,'baidu.html')

# 下载图片
# img_url = 'https://pics1.baidu.com/feed/a8773912b31bb05107bb739424d3deba4bede023.jpeg@f_auto?token=565d6232dee8588e4e7bf6acddbc6a1c'
# urllib.request.urlretrieve(url=img_url,filename='1.jpg')

# 下载视频
video_url = 'https://vdept3.bdstatic.com/mda-qeeazucx2fstth6s/sc/cae_h264/1715759308413434703/mda-qeeazucx2fstth6s.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1715874343-0-0-30ba7acbf02933d1f1d4dc86154f9fc3&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=2743862513&vid=17405445642028762441&klogid=2743862513&abtest='
urllib.request.urlretrieve(url=video_url,filename='video1.mp4')
