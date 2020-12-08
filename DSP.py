# Copyright 2020 Center for Intelligent and Networked Systems.
# This program is distributed under the Apache license 2.0.
# Supported by National Key Research and Development Project of China (No. 2017YFC0704100 entitled New generation intelligent building platform techniques) and the National Natural Science Foundation of China (No. 61425027), the 111 International Collaboration Program of China under Grant BP2018006.

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from IoTGUI import *

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())