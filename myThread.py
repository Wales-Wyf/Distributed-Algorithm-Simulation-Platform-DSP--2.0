# encoding: utf-8
from PyQt5 import QtCore
import socket
import json

class myThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(myThread, self).__init__(parent)
    text_signal = QtCore.pyqtSignal(str)

    def server(self):
        cont = """HTTP/1.1 200 OK\r\n\r\n"""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        localIP = socket.gethostbyname(socket.gethostname())
        s.bind((localIP, 50000))
        while 1:
            try:
                data, addr = s.recvfrom(100000000)
                jdata = json.loads(data)
            except Exception:
                print ("接收数据出错")
            else:
                if jdata["key"] == "runData":
                    self.text_signal.emit("Node" + str(jdata["id"]) + ": " + jdata["info"])
                else:
                    print ("数据有误")
        s.close()

    def run(self):
        self.server()
