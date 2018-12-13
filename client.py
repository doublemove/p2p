import socket

obj = socket.socket()

ip = "54.147.119.99"
# ip = "127.0.0.0"
obj.connect((ip, 12580))
print('connect sucess')
ret = str(obj.recv(1024), encoding = 'utf-8')

print(ret)