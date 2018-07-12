#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: work.py
#          Desc:
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-07-12 21:24:03
#       History:
# =============================================================================
'''
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
import xlwt
import sys


class Work(QMainWindow):
    def __init__(self):
        # 启动UI
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        # 绑定事件
        self.ui.gene_txt_pushButton.clicked.connect(self.gene_txt)
        self.ui.gene_xls_pushButton.clicked.connect(self.gene_xls)

    def hello(self):
        print('Hello!')

    def is_in_selected(self):
        if self.ui.in_radioButton.isChecked():
            return True
        else:
            return False

    def gene_txt(self, is_in=True, num=1, max_num=99, value=100):
        """
        生成txt文件
        """
        txt1 = '''
        //num号
        "BinDB".B_In[num].Sensor_F := In0;
        "BinDB".B_In[num].Lock_B := In1;
        "BinDB".B_In[num].Cage_D := In2;
        "BinDB".B_In[num].Cage_F := In3;
        "BinDB".B_In[num].Select :=In4;
        "BinDB".B_In[num].Switch :=In5;
        "BinDB".B_In[num].Estop := In6;
        "BinDB".B_In[num].Spare := In7;
        '''
        txt2 = '''
        //num号
        "BinDB".B_Out[num].Green := Ou0;
        "BinDB".B_Out[num].Yellow :=Ou1;
        "BinDB".B_Out[num].Red := Ou2;
        "BinDB".B_Out[num].Alarm := Ou3;
        "BinDB".B_Out[num].Push :=Ou4;
        "BinDB".B_Out[num].Pull := Ou5;
        "BinDB".B_Out[num].SpareA := Ou6;
        "BinDB".B_Out[num].SpareB := Ou7;
        '''
        # 判断是否为IN，否为OUT
        is_in = self.is_in_selected()
        # 起始值
        num_str = self.ui.num_lineEdit.text()
        # 最大值
        max_num_str = self.ui.max_num_lineEdit.text()
        # 基数
        value_str = self.ui.value_lineEdit.text()
        if num_str and max_num_str and value_str:
            num = int(num_str)
            max_num = int(max_num_str)
            value = int(value_str)
        # 保存txt分段值
        txt_list = []
        Total_Num = range(num, max_num + 1, 2)
        Begin_byte = value

        def gene_point(num, begin_byte):
            point = []
            for i in range(8):
                if num % 2:
                    value = begin_byte + (num - 1) / 2
                else:
                    value = begin_byte + (num - 2) / 2
                point.append('%I' + str(value + round(i / 10, 1)))
            return point

        for _num in Total_Num:
            if is_in:
                txt_mod = txt1.replace('num', str(_num))
                for i in range(8):
                    txt_mod = txt_mod.replace(
                        'In{}'.format(i), str(gene_point(_num, Begin_byte)[i]))
            else:
                txt_mod = txt2.replace('num', str(_num))
                for i in range(8):
                    txt_mod = txt_mod.replace(
                        'Ou{}'.format(i), str(gene_point(_num, Begin_byte)[i]))
            txt_list.append(txt_mod)
        filename = '110SCL.txt'
        with open(filename, 'w') as f:
            for item in txt_list:
                f.write(item)

    def gene_xls(self, num=1, max_num=99):
        """
        生成Excel文件
        """
        num_str = self.ui.num_lineEdit_2.text()
        max_num_str = self.ui.max_num_lineEdit_2.text()
        try:
            num = int(num_str)
            max_num = int(max_num_str)
        except:
            pass
        # 总行数
        if (max_num - num) % 2:
            total_row = 8 * ((max_num + 1 - num) / 2)
        else:
            total_row = 8 * (((max_num - num) / 2) + 1)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("Sheet")
        for i in range(int(total_row)):
            num_ = (i // 8) * 2 + num
            if i % 8 == 0:
                s = self.ui.value_lineEdit_01.text()
            elif i % 8 == 1:
                s = self.ui.value_lineEdit_02.text()
            elif i % 8 == 2:
                s = self.ui.value_lineEdit_03.text()
            elif i % 8 == 3:
                s = self.ui.value_lineEdit_04.text()
            elif i % 8 == 4:
                s = self.ui.value_lineEdit_05.text()
            elif i % 8 == 5:
                s = self.ui.value_lineEdit_06.text()
            elif i % 8 == 6:
                s = self.ui.value_lineEdit_07.text()
            elif i % 8 == 7:
                s = self.ui.value_lineEdit_08.text()
            sheet.write(i, 0, str(num_) + s)
        workbook.save("PLCtest.xls")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Work()
    sys.exit(app.exec_())
