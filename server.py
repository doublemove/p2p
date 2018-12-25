#encoding=utf-8
import SocketServer, time

ipPort = ('', 12580)

class Myserver(SocketServer.BaseRequestHandler):

    def handle(self):

        conn = self.request
        conn.sendall(bytes([u"你好，我是机器人",'1']))
        print conn.getsockname()
        ret_bytes = conn.recv(1024)
        ret_str = unicode(ret_bytes)
        print ret_str
        # if ret_str == "q":
            # break
        # conn.sendall(bytes(ret_str+"你好我好大家好"))

if __name__ == "__main__":
    print(u'啥事')
    server = SocketServer.ThreadingTCPServer(ipPort, Myserver)
    server.serve_forever()

