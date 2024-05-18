import time

localtime = time.localtime(time.time())
print("本地时间：",localtime)

print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))