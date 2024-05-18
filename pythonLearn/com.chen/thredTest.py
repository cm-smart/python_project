import threading
import time

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # 创建一个唱歌线程
    singThread = threading.Thread(target=sing,args=("我在唱歌",))
    # 创建一个跳舞线程
    danceThread = threading.Thread(target=dance,kwargs={"msg":"hello thread"})

    # 让线程去干活
    singThread.start()
    danceThread.start()

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("starting",self.name)
        print_time(self.name,self.counter,5)
        print("exiting",self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s:%s" % (threadName,time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1,"thread-1",1)
thread2 = myThread(2,"thread-2",2)

#开启线程
thread1.start()
thread2.start()

print("exiting main thread")



