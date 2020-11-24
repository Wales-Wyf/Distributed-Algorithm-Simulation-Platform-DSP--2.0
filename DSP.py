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