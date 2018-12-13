import socket

sk = socket.socket()
# ip = "10.175.157.128"
sk.bind(('', 12580))
print(sk)
sk.listen(5)

conn, address = sk.accept()
print(conn, address)
conn.sendall(bytes("hello", encoding = 'utf-8'))
