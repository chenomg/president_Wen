# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gekou_groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.gekou_groupBox.setObjectName("gekou_groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.gekou_groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 451, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.in_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.in_radioButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.in_radioButton.setChecked(True)
        self.in_radioButton.setObjectName("in_radioButton")
        self.verticalLayout_2.addWidget(self.in_radioButton)
        self.out_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.out_radioButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.out_radioButton.setObjectName("out_radioButton")
        self.verticalLayout_2.addWidget(self.out_radioButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.num_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.num_label.setObjectName("num_label")
        self.gridLayout_2.addWidget(self.num_label, 0, 0, 1, 1)
        self.num_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.num_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.num_lineEdit.setObjectName("num_lineEdit")
        self.gridLayout_2.addWidget(self.num_lineEdit, 0, 1, 1, 1)
        self.max_num_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.max_num_label.setObjectName("max_num_label")
        self.gridLayout_2.addWidget(self.max_num_label, 1, 0, 1, 1)
        self.max_num_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.max_num_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.max_num_lineEdit.setObjectName("max_num_lineEdit")
        self.gridLayout_2.addWidget(self.max_num_lineEdit, 1, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.value_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.value_label.setObjectName("value_label")
        self.horizontalLayout_4.addWidget(self.value_label)
        self.value_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.value_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit.setObjectName("value_lineEdit")
        self.horizontalLayout_4.addWidget(self.value_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.gene_txt_pushButton = QtWidgets.QPushButton(self.gekou_groupBox)
        self.gene_txt_pushButton.setGeometry(QtCore.QRect(460, 60, 99, 33))
        self.gene_txt_pushButton.setMaximumSize(QtCore.QSize(99, 33))
        self.gene_txt_pushButton.setObjectName("gene_txt_pushButton")
        self.horizontalLayout.addWidget(self.gekou_groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gekou_groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.gekou_groupBox_2.setObjectName("gekou_groupBox_2")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.gekou_groupBox_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 30, 481, 101))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(11, 11, 10, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.value_label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.value_label_7.setObjectName("value_label_7")
        self.gridLayout_3.addWidget(self.value_label_7, 0, 8, 1, 1)
        self.value_lineEdit_03 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.value_lineEdit_03.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit_03.setObjectName("value_lineEdit_03")
        self.gridLayout_3.addWidget(self.value_lineEdit_03, 0, 5, 1, 1)
        self.num_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.num_label_2.setObjectName("num_label_2")
        self.gridLayout_3.addWidget(self.num_label_2, 0, 0, 1, 1)
        self.value_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.value_label_2.setObjectName("value_label_2")
        self.gridLayout_3.addWidget(self.value_label_2, 1, 2, 1, 1)
        self.num_lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.num_lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.num_lineEdit_2.setObjectName("num_lineEdit_2")
        self.gridLayout_3.addWidget(self.num_lineEdit_2, 0, 1, 1, 1)
        self.value_label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.value_label_1.setObjectName("value_label_1")
        self.gridLayout_3.addWidget(self.value_label_1, 0, 2, 1, 1)
        self.value_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.value_label_3.setObjectName("value_label_3")
        self.gridLayout_3.addWidget(self.value_label_3, 0, 4, 1, 1)
        self.value_lineEdit_02 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.value_lineEdit_02.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit_02.setObjectName("value_lineEdit_02")
        self.gridLayout_3.addWidget(self.value_lineEdit_02, 1, 3, 1, 1)
        self.max_num_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.max_num_label_2.setObjectName("max_num_label_2")
        self.gridLayout_3.addWidget(self.max_num_label_2, 1, 0, 1, 1)
        self.max_num_lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.max_num_lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.max_num_lineEdit_2.setObjectName("max_num_lineEdit_2")
        self.gridLayout_3.addWidget(self.max_num_lineEdit_2, 1, 1, 1, 1)
        self.value_lineEdit_05 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.value_lineEdit_05.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit_05.setObjectName("value_lineEdit_05")
        self.gridLayout_3.addWidget(self.value_lineEdit_05, 0, 7, 1, 1)
        self.value_label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.value_label_4.setObjectName("value_label_4")
        self.gridLayout_3.addWidget(self.value_label_4, 1, 4, 1, 1)
        self.value_label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.value_label_5.setObjectName("value_label_5")
        self.gridLayout_3.addWidget(self.value_label_5, 0, 6, 1, 1)
        self.value_lineEdit_04 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.value_lineEdit_04.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit_04.setObjectName("value_lineEdit_04")
        self.gridLayout_3.addWidget(self.value_lineEdit_04, 1, 5, 1, 1)
        self.value_lineEdit_01 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.value_lineEdit_01.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit_01.setObjectName("value_lineEdit_01")
        self.gridLayout_3.addWidget(self.value_lineEdit_01, 0, 3, 1, 1)
        self.value_lineEdit_07 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.value_lineEdit_07.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit_07.setObjectName("value_lineEdit_07")
        self.gridLayout_3.addWidget(self.value_lineEdit_07, 0, 9, 1, 1)
        self.value_label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.value_label_6.setObjectName("value_label_6")
        self.gridLayout_3.addWidget(self.value_label_6, 1, 6, 1, 1)
        self.value_label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.value_label_8.setObjectName("value_label_8")
        self.gridLayout_3.addWidget(self.value_label_8, 1, 8, 1, 1)
        self.value_lineEdit_06 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.value_lineEdit_06.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit_06.setObjectName("value_lineEdit_06")
        self.gridLayout_3.addWidget(self.value_lineEdit_06, 1, 7, 1, 1)
        self.value_lineEdit_08 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.value_lineEdit_08.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lineEdit_08.setObjectName("value_lineEdit_08")
        self.gridLayout_3.addWidget(self.value_lineEdit_08, 1, 9, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_3)
        self.gene_xls_pushButton = QtWidgets.QPushButton(self.gekou_groupBox_2)
        self.gene_xls_pushButton.setGeometry(QtCore.QRect(480, 70, 80, 33))
        self.gene_xls_pushButton.setObjectName("gene_xls_pushButton")
        self.horizontalLayout_2.addWidget(self.gekou_groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "闻总专用"))
        self.gekou_groupBox.setTitle(_translate("MainWindow", "格口信息一"))
        self.in_radioButton.setText(_translate("MainWindow", "IN"))
        self.out_radioButton.setText(_translate("MainWindow", "OUT"))
        self.num_label.setText(_translate("MainWindow", "初始序号\n"
"like: 1 or 2"))
        self.num_lineEdit.setText(_translate("MainWindow", "1"))
        self.max_num_label.setText(_translate("MainWindow", "最大序号"))
        self.max_num_lineEdit.setText(_translate("MainWindow", "99"))
        self.value_label.setText(_translate("MainWindow", "初始值\n"
"like: 100"))
        self.value_lineEdit.setText(_translate("MainWindow", "100"))
        self.gene_txt_pushButton.setText(_translate("MainWindow", "生成txt"))
        self.gekou_groupBox_2.setTitle(_translate("MainWindow", "格口信息二"))
        self.value_label_7.setText(_translate("MainWindow", "值7"))
        self.value_lineEdit_03.setText(_translate("MainWindow", "#锁格"))
        self.num_label_2.setText(_translate("MainWindow", "初始序号\n"
"like: 1 or 2"))
        self.value_label_2.setText(_translate("MainWindow", "值2"))
        self.num_lineEdit_2.setText(_translate("MainWindow", "1"))
        self.value_label_1.setText(_translate("MainWindow", "值1"))
        self.value_label_3.setText(_translate("MainWindow", "值3"))
        self.value_lineEdit_02.setText(_translate("MainWindow", "#满槽"))
        self.max_num_label_2.setText(_translate("MainWindow", "最大序号"))
        self.max_num_lineEdit_2.setText(_translate("MainWindow", "99"))
        self.value_lineEdit_05.setText(_translate("MainWindow", "#气缸"))
        self.value_label_4.setText(_translate("MainWindow", "值4"))
        self.value_label_5.setText(_translate("MainWindow", "值5"))
        self.value_lineEdit_04.setText(_translate("MainWindow", "#维修"))
        self.value_lineEdit_01.setText(_translate("MainWindow", "#光电"))
        self.value_lineEdit_07.setText(_translate("MainWindow", "#A"))
        self.value_label_6.setText(_translate("MainWindow", "值6"))
        self.value_label_8.setText(_translate("MainWindow", "值8"))
        self.value_lineEdit_06.setText(_translate("MainWindow", "#确认"))
        self.value_lineEdit_08.setText(_translate("MainWindow", "#B"))
        self.gene_xls_pushButton.setText(_translate("MainWindow", "生成XLS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

