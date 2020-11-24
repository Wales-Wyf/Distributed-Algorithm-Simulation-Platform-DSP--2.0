import sys
import codecs
import os
import io
import time
import json
import myThread
import socket
import myThread2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QWidget,QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pysnooperDB import DataBaseFunc as DB
from subprocess import run

class Ui_controlbutton(object):
    def setupUi(self, controlbutton):
        controlbutton.setObjectName("controlbutton")
        controlbutton.resize(659, 393)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(controlbutton)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(controlbutton)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nodeNum = QtWidgets.QLineEdit(controlbutton)
        self.nodeNum.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeNum.sizePolicy().hasHeightForWidth())
        self.nodeNum.setSizePolicy(sizePolicy)
        self.nodeNum.setAlignment(QtCore.Qt.AlignCenter)
        self.nodeNum.setObjectName("nodeNum")
        self.horizontalLayout.addWidget(self.nodeNum)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(controlbutton)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.mainNode = QtWidgets.QLineEdit(controlbutton)
        self.mainNode.setEnabled(False)
        self.mainNode.setAlignment(QtCore.Qt.AlignCenter)
        self.mainNode.setObjectName("mainNode")
        self.horizontalLayout.addWidget(self.mainNode)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(controlbutton)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.downloadTopology = QtWidgets.QPushButton(controlbutton)
        self.downloadTopology.setMinimumSize(QtCore.QSize(0, 40))
        self.downloadTopology.setObjectName("downloadTopology")
        self.horizontalLayout_2.addWidget(self.downloadTopology)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.uploadTopology = QtWidgets.QPushButton(controlbutton)
        self.uploadTopology.setMinimumSize(QtCore.QSize(0, 40))
        self.uploadTopology.setObjectName("uploadTopology")
        self.horizontalLayout_2.addWidget(self.uploadTopology)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(controlbutton)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.downloadAlgorithm = QtWidgets.QPushButton(controlbutton)
        self.downloadAlgorithm.setMinimumSize(QtCore.QSize(0, 40))
        self.downloadAlgorithm.setObjectName("downloadAlgorithm")
        self.horizontalLayout_3.addWidget(self.downloadAlgorithm)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.uploadAlgorithm = QtWidgets.QPushButton(controlbutton)
        self.uploadAlgorithm.setMinimumSize(QtCore.QSize(0, 40))
        self.uploadAlgorithm.setObjectName("uploadAlgorithm")
        self.horizontalLayout_3.addWidget(self.uploadAlgorithm)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.run = QtWidgets.QPushButton(controlbutton)
        self.run.setMinimumSize(QtCore.QSize(0, 50))
        self.run.setObjectName("run")
        self.verticalLayout.addWidget(self.run)
        self.quit = QtWidgets.QPushButton(controlbutton)
        self.quit.setMinimumSize(QtCore.QSize(0, 50))
        self.quit.setObjectName("quit")
        self.verticalLayout.addWidget(self.quit)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)

        self.retranslateUi(controlbutton)

    def retranslateUi(self, controlbutton):
        _translate = QtCore.QCoreApplication.translate
        controlbutton.setWindowTitle(_translate("controlbutton", "分布式仿真平台"))
        self.label.setText(_translate("controlbutton", "节点个数："))
        self.label_5.setText(_translate("controlbutton", "主节点："))
        self.mainNode.setText(_translate("controlbutton", "1"))
        self.label_2.setText(_translate("controlbutton", "拓扑信息："))
        self.downloadTopology.setText(_translate("controlbutton", "模板格式"))
        self.uploadTopology.setText(_translate("controlbutton", "上传拓扑"))
        self.label_3.setText(_translate("controlbutton", "算法程序："))
        self.downloadAlgorithm.setText(_translate("controlbutton", "模板格式"))
        self.uploadAlgorithm.setText(_translate("controlbutton", "上传算法"))
        self.run.setText(_translate("controlbutton", "运行"))
        self.quit.setText(_translate("controlbutton", "退出"))

class controlbutton(QWidget,Ui_controlbutton):
    def __init__(self):
        super(controlbutton, self).__init__()
        self.setupUi(self)

class textwidget(QtWidgets.QWidget):
    def __init__(self):
        super(textwidget, self).__init__()
        self.setObjectName("textwidget")
        self.resize(400, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("textwidget", "Form"))


class Ui_MainWindow(object):
    tpFlag = 0
    agFlag = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.userlineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userlineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.userlineEdit.setObjectName("userlineEdit")
        self.horizontalLayout.addWidget(self.userlineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.passwdlineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwdlineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.passwdlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdlineEdit.setObjectName("passwdlineEdit")
        self.horizontalLayout.addWidget(self.passwdlineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.databaselineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.databaselineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.databaselineEdit.setObjectName("databaselineEdit")
        self.horizontalLayout.addWidget(self.databaselineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.tablenamelineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.tablenamelineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.tablenamelineEdit.setObjectName("tablenamelineEdit")
        self.horizontalLayout.addWidget(self.tablenamelineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 3)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 3)
        self.horizontalLayout.setStretch(8, 1)
        self.horizontalLayout.setStretch(9, 1)
        self.horizontalLayout.setStretch(10, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.variablelineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.variablelineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.variablelineEdit.setObjectName("variablelineEdit")
        self.horizontalLayout_2.addWidget(self.variablelineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 15)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.showtablepushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.showtablepushButton.setObjectName("showtablepushButton")
        self.horizontalLayout_4.addWidget(self.showtablepushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.tablename2lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.tablename2lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.tablename2lineEdit.setObjectName("tablename2lineEdit")
        self.horizontalLayout_4.addWidget(self.tablename2lineEdit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.selectpushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.selectpushButton.setObjectName("selectpushButton")
        self.horizontalLayout_4.addWidget(self.selectpushButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.deletepushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.deletepushButton.setObjectName("deletepushButton")
        self.horizontalLayout_4.addWidget(self.deletepushButton)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 3)
        self.horizontalLayout_4.setStretch(5, 1)
        self.horizontalLayout_4.setStretch(6, 3)
        self.horizontalLayout_4.setStretch(7, 1)
        self.horizontalLayout_4.setStretch(8, 3)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #创建QDockWidget窗口（标题，自身窗口）
        self.items=QDockWidget('控制按钮',self)
        self.items2=QDockWidget('运行状态',self)
        self.items3=QDockWidget('运行结果',self)

        self.Widget=controlbutton()
        self.Widget2=textwidget()
        self.Widget3=textwidget()

        #在窗口区域设置QWidget，添加列表控件
        self.items.setWidget(self.Widget)
        self.items2.setWidget(self.Widget2)
        self.items3.setWidget(self.Widget3)
        #设置dock窗口是否可以浮动，True，运行浮动在外面，自动与主界面脱离，False，默认浮动主窗口内，可以手动脱离
        self.items.setFloating(False)
        self.items2.setFloating(False)
        self.items3.setFloating(False)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.items)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.items2)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.items3)

        self.retranslateUi(MainWindow)
        
        self.Widget.downloadTopology.clicked.connect(self.downTopology)
        self.Widget.uploadTopology.clicked.connect(self.upTopology)
        self.Widget.downloadAlgorithm.clicked.connect(self.downAlgorithm)
        self.Widget.uploadAlgorithm.clicked.connect(self.upAlgorithm)
        self.Widget.run.clicked.connect(self.runAlgorithm)
        self.Widget.quit.clicked.connect(self.close)
        self.showtablepushButton.clicked.connect(self.showtablesname)
        self.selectpushButton.clicked.connect(self.showtable)
        self.deletepushButton.clicked.connect(self.deletetable)
        self.pushButton.clicked.connect(self.helpinput)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.thread = myThread.myThread()
        self.thread.text_signal.connect(self.updateRunInfo)
        self.thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "分布式仿真平台"))
        self.label_6.setText(_translate("MainWindow", "调试模式开关   "))
        self.groupBox.setTitle(_translate("MainWindow", "调试模式信息输入"))
        self.label.setText(_translate("MainWindow", "数据库用户名："))
        self.userlineEdit.setText(_translate("MainWindow", "root"))
        self.label_2.setText(_translate("MainWindow", "数据库密码："))
        self.passwdlineEdit.setText(_translate("MainWindow", "root"))
        self.label_3.setText(_translate("MainWindow", "数据库名："))
        self.databaselineEdit.setText(_translate("MainWindow", "TESTDB"))
        self.label_4.setText(_translate("MainWindow", "数据表前缀名："))
        self.tablenamelineEdit.setText(_translate("MainWindow", "algorithm1"))
        self.label_5.setText(_translate("MainWindow", "查看变量名："))
        self.pushButton.setText(_translate("MainWindow", "输入提示"))
        self.groupBox_2.setTitle(_translate("MainWindow", "调试模式显示控制"))
        self.showtablepushButton.setText(_translate("MainWindow", "显示所有数据表"))
        self.label_7.setText(_translate("MainWindow", "数据表名："))
        self.selectpushButton.setText(_translate("MainWindow", "查询"))
        self.deletepushButton.setText(_translate("MainWindow", "删除"))
        self.groupBox_3.setTitle(_translate("MainWindow", "调试信息显示"))


    def downTopology(self):
        self.example_tp = topology_example()
        self.example_tp.show()

    def upTopology(self):
        if self.Widget.nodeNum.text().isdigit() and int(self.Widget.nodeNum.text()) > 0:
            try:
                self.tp = topology_up(self.Widget.nodeNum.text())
                self.tp.show()
                self.tpFlag = 1
            except Exception:
                QtWidgets.QMessageBox.information(self.centralwidget, "提示", "写入拓扑出错")
        else:
            QtWidgets.QMessageBox.information(self.centralwidget, "提示", "请输入正确的节点个数")

    def downAlgorithm(self):
        self.example_ag = algorithm_example()
        self.example_ag.show()

    def upAlgorithm(self):
        path = os.getcwd() + "\\IoT\\question.py"
        fileName = QtWidgets.QFileDialog.getOpenFileName()
        self.agFlag = 1
        if fileName[0] != "":
            try:
                text = codecs.open(fileName[0], 'r', 'utf-8').read()
            except Exception:
                QtWidgets.QMessageBox.information(self.centralwidget, "提示", "无法读取指定文件")
            file = codecs.open(path, 'w', 'utf-8')
            file.write(text)
            file.close()
            self.agFlag = 1

    def runAlgorithm(self):
        try:
            pid = os.getpid()
            run('taskkill /F /im python.exe /FI ' + '"PID ne ' + str(pid) + '"',shell=True)
        except Exception:
            QtWidgets.QMessageBox.information(self.centralwidget, "提示", "调用系统指令失败")
        self.Widget2.textEdit.clear()
        self.Widget3.textEdit.clear()
        if self.Widget.nodeNum.text().isdigit() and self.Widget.mainNode.text().isdigit():
            num = self.Widget.nodeNum.text()
            mainNode = self.Widget.mainNode.text()
            if int(num) < 0 or int(mainNode) < 0 or int(mainNode) > int(num):
                QtWidgets.QMessageBox.information(self.centralwidget, "提示", "请输入正确的节点个数")
                return
        else:
            QtWidgets.QMessageBox.information(self.centralwidget, "提示", "请输入正确的节点个数")
            return
        if self.tpFlag == 0:
            QtWidgets.QMessageBox.information(self.centralwidget, "提示", "请导入拓扑")
            return
        if self.agFlag == 0:
            QtWidgets.QMessageBox.information(self.centralwidget, "提示", "请导入算法")
            return
        try:
            # 删除start in debug mode行
            path = os.getcwd() + "\\IoT\\debug.txt"
            with open(path,"r") as f:
                lines = f.readlines()
            with open(path,"w") as f_w:
                for line in lines:
                    if "start in debug mode" in line:
                        continue
                    f_w.write(line)
                    
            if self.radioButton.isChecked():
                if not self.confirmdb():
                    return
                with open( path, 'a+') as f:
                    f.write("start in debug mode\n")
            run("start .\IoT\start.vbs " + num,shell=True)
        except OSError:
            QtWidgets.QMessageBox.information(self.centralwidget, "提示", "执行脚本文件出错")
        else:
            QtWidgets.QMessageBox.information(self.centralwidget, "提示", "节点服务器正在启动，请等待算法结果")
            time.sleep(5)
            self.thread2 = myThread2.myThread2()
            self.thread2.text_signal.connect(self.getResult)
            self.thread2.start()

    def updateRunInfo(self, text):
        self.Widget2.textEdit.append(text)

    def getResult(self, text):
        pid = os.getpid()
        if text == "0":
            QtWidgets.QMessageBox.information(self.centralwidget, "提示", "程序编写出错，请检查导入拓扑所用端口是否能正常使用，导入算法是否具有语法问题，以及系统是否具有算法所需的python模块")
            run('taskkill /F /im python.exe /FI ' + '"PID ne ' + str(pid) + '"',shell=True)
        else:
            self.Widget3.textEdit.setPlainText(text)
            run('taskkill /F /im python.exe /FI ' + '"PID ne ' + str(pid) + '"',shell=True)


    def confirmdb(self):
        try:
            DB.create_table(self.tablenamelineEdit.text(), user= self.userlineEdit.text(), \
            passwd=self.passwdlineEdit.text(),databasename = self.databaselineEdit.text())
        except Exception:
            QtWidgets.QMessageBox.information(self, "提示", "数据库信息输入有误，请检查数据库用户名、密码、数据库名是否输入正确，数据库密码请注意大小写")
            return 0
        else:
            DB.delete_table(self.tablenamelineEdit.text(), user= self.userlineEdit.text(), \
            passwd=self.passwdlineEdit.text(),databasename = self.databaselineEdit.text())

            text = self.userlineEdit.text() + "\r\n"
            text = text + self.passwdlineEdit.text() + "\r\n"
            text = text + self.databaselineEdit.text() + "\r\n"
            text = text +  self.tablenamelineEdit.text() + "\r\n"

            text2 = self.variablelineEdit.text()
            text2 = text2.replace('\n','')
            text2 = text2.replace(' ','')
            variablelist = text2.split(",")

            for i in range(len(variablelist)):
                text = text + variablelist[i] + "\r\n"

            path = os.getcwd() + "\IoT\\debug.txt"
            try:
                file = codecs.open(path, 'w', 'utf-8')
                file.write(text)
                file.close()
            except IOError:
                QtWidgets.QMessageBox.information(self, "提示", "无法写入文件")
                return 0
            else:
                return 1

    def showtablesname(self):
        try:
            tables = DB.show_tablename(user= self.userlineEdit.text(),passwd=self.passwdlineEdit.text(),databasename = self.databaselineEdit.text())
        except Exception:
            QtWidgets.QMessageBox.information(self, "提示", "信息输入有误，请检查数据库用户名、密码、数据库名是否输入正确")
            return
        col = 1
        row = len(tables)
        self.tableWidget.setRowCount(row-1)
        self.tableWidget.setColumnCount(col)
        tablehead = []
        tablehead.append(tables[0])
        self.tableWidget.setHorizontalHeaderLabels(tablehead)
        # self.table.verticalHeader().setVisible(False)
        for i in range(1,row):
            data=QTableWidgetItem(str(tables[i]))
            self.tableWidget.setItem(i-1,0,data)

        # 优化 5 将行与列的高度设置为所显示的内容的宽度高度匹配
        QTableWidget.resizeColumnsToContents(self.tableWidget)


    def showtable(self):
        tablename = self.tablename2lineEdit.text()
        try:
            tables = DB.show_table(tablename, user= self.userlineEdit.text(),passwd=self.passwdlineEdit.text(),databasename = self.databaselineEdit.text())
        except Exception:
            QtWidgets.QMessageBox.information(self, "提示", "信息输入有误，请检查数据库用户名、密码、数据库名、数据表名是否输入正确\n此外，本程序只保证正确显示本程序产生的数据表，其他数据表的显示可能会有问题")
            return

        col = len(tables[0])
        row = len(tables)

        self.tableWidget.setRowCount(row-1)
        self.tableWidget.setColumnCount(col-1)
        tablehead = tables[0]
        tablehead.pop(0)
        self.tableWidget.setHorizontalHeaderLabels(tablehead)
        # self.table.verticalHeader().setVisible(False)
        for i in range(1,row):
            for j in range(1,col):
                data=QTableWidgetItem(str(tables[i][j])) 
                self.tableWidget.setItem(i-1,j-1,data)
        QTableWidget.resizeColumnsToContents(self.tableWidget)


    def deletetable(self):
        try:
            tablename = self.tablename2lineEdit.text()
            tables = DB.delete_table(tablename, user= self.userlineEdit.text(),passwd=self.passwdlineEdit.text(),databasename = self.databaselineEdit.text())
        except Exception:
            QtWidgets.QMessageBox.information(self, "提示", "信息输入有误，请检查数据库用户名、密码、数据库名、数据表名是否输入正确")
        else:
            QtWidgets.QMessageBox.information(self, "提示", "数据表%s删除成功"%(tablename))

    def helpinput(self):
        QtWidgets.QMessageBox.information(self, "输入提示", "英文逗号分割变量名\n例如：x,m,adjData\n文本框为空则记录所有变量")



class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


class topology_example(QtWidgets.QWidget):
    def __init__(self):
        super(topology_example, self).__init__()
        self.setObjectName("example_tp")
        self.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 700, 550))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setWindowTitle("拓扑模板格式")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setHtml(_translate("showTopology",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Menlo\'; color:#000000; background-color:#ffffff;\">[</span><span style=\" font-family:\'Menlo\'; color:#000000;\"><br />   {<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;_comment&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#008000;\">&quot;_comment中的文字仅作为注释，实际导入中可删去。拓扑请使用json数据格式进行导入，具体形式为每个节点描述组成的数组。&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;_comment2&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#008000;\">&quot;单个节点具体格式如下所示，ID为1~n的编号；IP为该节点IP；PORT为给该节点指定的6个通信服务器与1个任务服务器的端口数组；adjID为该节点邻接节点数组，要求对称性；adjDirection为邻居节点对应的端口编号，需在1~6中取值；datalist为该节点初始化时需传入的数据，格式自定。接下来为实例，指定一个正方形中的连接关系&quot;<br />   </span><span style=\" font-family:\'Menlo\'; color:#000000;\">},<br />   {<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;ID&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">1</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;IP&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#008000;\">&quot;localhost&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;PORT&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10000</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10001</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10002</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10003</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10004</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10005</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10006</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;adjID&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">2</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">3</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;adjDirection&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">1</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">2</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;datalist&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: {}<br />   },<br />   {<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;ID&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">2</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;IP&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#008000;\">&quot;localhost&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;PORT&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10007</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10008</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10009</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10010</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10011</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10012</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10013</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;adjID&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">1</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">4</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;adjDirection&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">3</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">2</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;datalist&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: {}<br />   },<br />   {<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;ID&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">3</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;IP&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#008000;\">&quot;localhost&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;PORT&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10014</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10015</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10016</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10017</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10018</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10019</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10020</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;adjID&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">1</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">4</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;adjDirection&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">4</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">1</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;datalist&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: {}<br />   },<br />   {<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;ID&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">4</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;IP&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#008000;\">&quot;localhost&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">,<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;PORT&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10021</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10022</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10023</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10024</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10025</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10026</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">10027</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;adjID&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">2</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">3</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;adjDirection&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: [</span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">4</span><span style=\" font-family:\'Menlo\'; color:#000000;\">, </span><span style=\" font-family:\'Menlo\'; color:#0000ff;\">3</span><span style=\" font-family:\'Menlo\'; color:#000000;\">],<br />      </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#660e7a;\">&quot;datalist&quot;</span><span style=\" font-family:\'Menlo\'; color:#000000;\">: {}<br />   }<br />]</span></p></body></html>"))


class algorithm_example(QtWidgets.QWidget):
    def __init__(self):
        super(algorithm_example, self).__init__()
        self.setObjectName("example_ag")
        self.resize(800, 600)
        self.setWindowTitle("算法模板格式")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 700, 550))
        self.textEdit.setObjectName("textEdit")
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setHtml(_translate("showAlgorithm",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Menlo\'; font-style:italic; color:#808080;\"># import需求模块<br /><br /># 用户自定义函数区<br />&quot;&quot;&quot;<br />用户编码区域<br />&quot;&quot;&quot;<br /><br /># 定义算法主函数taskFunction(self,id,adjDirection,datalist)，四个形参分别为节点类，节点ID，节点邻居对应的方向以及初始化时键入的数据<br /></span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#000080;\">def </span><span style=\" font-family:\'Menlo\'; color:#000000;\">taskFunction(self, id, adjDirection, datalist):<br />    </span><span style=\" font-family:\'Menlo\'; font-style:italic; color:#808080;\"># 在算法设计中，可与邻居节点进行通信，函数为self.transmitData(data)，data为需通信数据，可为字符串、对象、数组等JSON格式能解析的数据类型<br />    # 返回数据feedback = self.transmitData(data)为二元数组，第一分量表示返回邻居方向adjDirection，第二分量表示相应数据,与第一分量中方向一一对应型<br />    # 通信的异步函数为self.sendDataToDirection(direction,data),direction为需要传递数据的方向，data为需通信数据，可为字符串，对象，数组等JSON格式能解析的数据类型，调用该函数时可通过self.adjData获取邻居传递过来的数据信息，内容与方向adjDirection一一对应<br />    # 异步通信函数请勿与同步通信函数同时使用，使用异步通信函数时需要考虑到程序执行的异步性与延时，慎用！<br />    # 调用异步函数时可以使用self.syncNode()函数使得程序实现同步<br />    # 在算法设计中，可在运行状态区域打印出自己调试所需要的算法运行信息，函数为self.sendUDP(str)，str为字符串格式的数据<br /><br />    </span><span style=\" font-family:\'Menlo\'; color:#000000;\">value = []<br />    </span><span style=\" font-family:\'Menlo\'; font-style:italic; color:#808080;\"># value为返回值，可为任意格式<br /><br />    </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#008000;\">&quot;&quot;&quot;<br />    用户编码区域<br />    &quot;&quot;&quot;<br /><br />    </span><span style=\" font-family:\'Menlo\'; font-weight:600; color:#000080;\">return </span><span style=\" font-family:\'Menlo\'; color:#000000;\">value</span></p></body></html>"))

class topology_up(QtWidgets.QWidget):
    def __init__(self, data):
        super(topology_up, self).__init__()
        self.setObjectName("showTopology")
        self.resize(667, 556)
        self.setWindowTitle("拓扑输入")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(59, 39, 551, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.confirm = QtWidgets.QPushButton(self)
        self.confirm.setGeometry(QtCore.QRect(190, 490, 81, 41))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setGeometry(QtCore.QRect(370, 490, 81, 41))
        self.cancel.setObjectName("cancel")


        self.confirm.clicked.connect(self.confirmTP)
        self.cancel.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.confirm.setText(_translate("showTopology", "确定"))
        self.cancel.setText(_translate("showTopology", "取消"))

        self.num = int(data)

    def confirmTP(self):
        text = self.textEdit.toPlainText()
        IP = []
        PORT = []
        ID = []
        adjID = []
        datalist = []
        try:
            js = json.loads(text)
        except Exception:
            QtWidgets.QMessageBox.information(self, "提示", "给定的拓扑文件需为json格式")
            return
        else:
            for ele in js:
                if "ID" in ele:
                    try:
                        ID.append(ele["ID"])
                        IP.append(ele["IP"])
                        PORT.append(ele["PORT"])
                        adjID.append(ele["adjID"])
                        datalist.append(ele["datalist"])
                    except Exception:
                        try:
                            a = str(ele["ID"])
                        except Exception:
                            QtWidgets.QMessageBox.information(self, "提示", "节点ID不正确")
                            return
                        else:
                            QtWidgets.QMessageBox.information(self, "提示", "ID为" + str(ele["ID"]) + "的节点信息不全")
                            return
                    if len(ele["PORT"]) != 7:
                        QtWidgets.QMessageBox.information(self, "提示",
                                                          "ID为" + str(ele["ID"]) + "的节点端口数不为7")
                        return
                    if len(ele["adjID"]) > 6:
                        QtWidgets.QMessageBox.information(self, "提示",
                                                          "ID为" + str(ele["ID"]) + "的节点相邻节点个数应不多于6")
                        return

            if len(ID) != self.num:
                QtWidgets.QMessageBox.information(self, "提示",
                                                  "拓扑中节点数量与所输入数量不匹配")
                return
            for i in range(len(ID)):
                for tmp in adjID[i]:
                    flag = 0
                    for ele in js:
                        if "ID" in ele:
                            if ele["ID"] == tmp:
                                flag = 1
                                if ID[i] not in ele["adjID"]:
                                    QtWidgets.QMessageBox.information(self, "提示",
                                                                      "节点" + str(ID[i]) + "与" + str(tmp) + "不保证对称性")
                                    return
                    if flag == 0:
                        QtWidgets.QMessageBox.information(self, "提示", "节点" + str(ID[i]) + "的邻居节点有误")
                        return
            for i in range(len(ID)):
                for j in range(i+1 ,len(ID)):
                    for k in range(7):
                        for l in range(7):
                            if PORT[i][k] == PORT[j][l]:
                                if IP[i] == IP[j]:
                                    QtWidgets.QMessageBox.information(self, "提示", "节点" + str(ID[i]) + "与节点" + str(ID[j]) + "有端口完全相同")
                                    return
                            if PORT[i][k] == PORT[i][l]:
                                if k != l:
                                    QtWidgets.QMessageBox.information(self, "提示",
                                                                      "节点" + str(ID[i]) + "有端口完全相同")
                                    return
        path = os.getcwd() + "\IoT\\topology.txt"
        try:
            file = codecs.open(path, 'w', 'utf-8')
            file.write(text)
            file.close()
        except IOError:
            QtWidgets.QMessageBox.information(self, "提示", "无法读取指定文件")
        self.close()

