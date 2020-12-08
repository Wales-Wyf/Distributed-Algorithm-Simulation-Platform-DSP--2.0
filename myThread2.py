# Copyright 2020 Center for Intelligent and Networked Systems, Department of Automation, Tsinghua University, Beijing, China.
# This program is distributed under the Apache license 2.0.
# Supported by National Key Research and Development Project of China (No. 2017YFC0704100 entitled New generation intelligent building platform techniques) and the National Natural Science Foundation of China (No. 61425027), the 111 International Collaboration Program of China under Grant BP2018006.
# encoding: utf-8

from PyQt5 import QtCore,QtWidgets
import os
import json
import socket
import urllib.request
import http.client
import urllib.request
import requests
import time


class myThread2(QtCore.QThread):
    def __init__(self, parent=None):
        super(myThread2, self).__init__(parent)
    text_signal = QtCore.pyqtSignal(str)

    def run(self):
        localIP = socket.gethostbyname(socket.gethostname())
        GUIinfo = [localIP, 50000]
        data = {
            "key": "task",
            "GUIinfo": GUIinfo,
            "taskID": "question"
        }
        requrl = "http://" + localIP + ":10006"
        headerdata = {"Content-Type": "application/json"}
        # request = urllib.request.Request(url=requrl, headers=headerdata, data=json.dumps(data).encode("utf-8"))
        i=1
        while i==1:
            i = 0
            try:
                # response = urllib.request.urlopen(request)
                r = requests.post(requrl,data = json.dumps(data))
            except (urllib.request.URLError, http.client.BadStatusLine):
                self.text_signal.emit("0")
            except  Exception:
                i = 1
            else:
                # res = response.read()
                res2 = r.text
                self.text_signal.emit(str(res2))