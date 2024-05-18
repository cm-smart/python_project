import socket

# 创建socket对象
socketServer = socket.socket()
# 获取本地主机名
host = "localhost"
# 设置端口
port = 12345
# 绑定端口
socketServer.bind((host, port))

# 等待客户端连接
socketServer.listen(5)

# 建立客户端连接，返回一个元组
conn, addr = socketServer.accept()
print("连接地址：", addr)

while True:
    # 接收客户端消息，要使用客户端和服务端本次链接对象，而非socket
    data = conn.recv(1024).decode("UTF-8") # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法UTF-8编码，将字节数组转为字符串
    print("接收客户端消息：",data)
    # 向客户端发送回复消息
    msg = input("请输入你要和客户端回复的消息：") # encode将字符串编码转为字节数组对象
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

# 关闭连接
conn.close()
socketServer.close()