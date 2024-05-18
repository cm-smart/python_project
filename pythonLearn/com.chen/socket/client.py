import socket

socketClient = socket.socket()
host = "localhost"
port = 12345

socketClient.connect((host,port))
print("链接成功")

# 向服务端发送消息
msg = input("请输入向服务端发送的消息：")
socketClient.send(msg.encode("UTF-8"))
# 从服务端接收的消息
recvMsg = socketClient.recv(1024).decode("UTF-8")
print("从服务端接收的消息：",recvMsg)
socketClient.close()