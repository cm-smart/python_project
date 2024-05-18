import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self,threadId,name,q):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.q = q

    def run(self):
        print("starting ",self.name)
        process_data(self.name,self.q)
        print("exiting ",self.name)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName,data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["thread-1", "thread-2", "thread-3"]
nameList = ["one", "two", "three", "four", "five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)

threads = []
threadId = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadId,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("exiting main thread")