#encoding=utf-8
import socketserver, time

ipPort = ('', 12580)

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):

        conn = self.request
        conn.sendall(bytes([u"你好，我是机器人",'1']))
        print conn
        while True:
            time.sleep(1)
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes)
            if ret_str == "q":
                break
            conn.sendall(bytes(ret_str+"你好我好大家好"))

if __name__ == "__main__":
    print(u'啥事')
    server = socketserver.ThreadingTCPServer(ipPort, Myserver)
    server.serve_forever()

