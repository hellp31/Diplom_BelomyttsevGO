# Form implementation generated from reading ui file 'window/RegWin.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegWin(object):
    def setupUi(self, RegWin):
        RegWin.setObjectName("RegWin")
        RegWin.resize(497, 617)
        self.label_2 = QtWidgets.QLabel(parent=RegWin)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(-20, 0, 521, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 50pt \"Times New Roman\";\n"
"background-color: grey;\n"
"color: white;\n"
"text-align: center;\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(parent=RegWin)
        self.textEdit.setGeometry(QtCore.QRect(130, 120, 271, 41))
        self.textEdit.setStyleSheet(" background-color: #f6f6f6; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"  color: #000000;\n"
"font: 12pt \"Times New Roman\";\n"
" padding-left: 10px;\n"
"outline: none;\n"
"  border: 1px solid black;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=RegWin)
        self.label.setGeometry(QtCore.QRect(140, 100, 41, 21))
        self.label.setStyleSheet("font-weight: bold;\n"
"font:  12pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=RegWin)
        self.label_3.setGeometry(QtCore.QRect(140, 310, 41, 21))
        self.label_3.setStyleSheet("font-weight: bold;\n"
"font:  12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=RegWin)
        self.textEdit_3.setGeometry(QtCore.QRect(130, 190, 271, 41))
        self.textEdit_3.setStyleSheet(" background-color: #f6f6f6; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"  color: #000000;\n"
"font: 12pt \"Times New Roman\";\n"
"\n"
"outline: none;\n"
"  border: 1px solid black;\n"
" padding-left: 10px;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=RegWin)
        self.label_4.setGeometry(QtCore.QRect(140, 170, 51, 21))
        self.label_4.setStyleSheet("font-weight: bold;\n"
"font:  12pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.textEdit_4 = QtWidgets.QTextEdit(parent=RegWin)
        self.textEdit_4.setGeometry(QtCore.QRect(130, 260, 271, 41))
        self.textEdit_4.setStyleSheet(" background-color: #f6f6f6; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"  color: #000000;\n"
"font: 12pt \"Times New Roman\";\n"
"  padding-left: 10px;\n"
"outline: none;\n"
"  border: 1px solid black;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_5 = QtWidgets.QLabel(parent=RegWin)
        self.label_5.setGeometry(QtCore.QRect(140, 240, 61, 21))
        self.label_5.setStyleSheet("font-weight: bold;\n"
"font:  12pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=RegWin)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 450, 221, 41))
        self.pushButton_2.setStyleSheet(" background-color: #f6f6f6; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"\n"
"  width: 250px;\n"
"  height: 30px;\n"
"  padding-left: 10px;\n"
"outline: none;\n"
"  border: 1px solid black;\n"
"font-weight: bold;\n"
"font:  12pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(parent=RegWin)
        self.pushButton.setGeometry(QtCore.QRect(10, 560, 211, 41))
        self.pushButton.setStyleSheet(" background-color: #f6f6f6; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"  width: 250px;\n"
"  height: 30px;\n"
"  padding-left: 10px;\n"
"outline: none;\n"
"  border: 1px solid black;\n"
"font-weight: bold;\n"
"font:  12pt \"Times New Roman\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(parent=RegWin)
        self.label_6.setGeometry(QtCore.QRect(110, 420, 261, 31))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(parent=RegWin)
        self.comboBox.setGeometry(QtCore.QRect(140, 340, 111, 22))
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(parent=RegWin)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 400, 111, 22))
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_7 = QtWidgets.QLabel(parent=RegWin)
        self.label_7.setGeometry(QtCore.QRect(140, 370, 71, 21))
        self.label_7.setStyleSheet("font-weight: bold;\n"
"font:  12pt \"Times New Roman\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=RegWin)
        self.label_8.setGeometry(QtCore.QRect(190, 99, 211, 21))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=RegWin)
        self.label_9.setGeometry(QtCore.QRect(190, 170, 211, 21))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=RegWin)
        self.label_10.setGeometry(QtCore.QRect(200, 240, 201, 21))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=RegWin)
        self.label_11.setGeometry(QtCore.QRect(180, 310, 201, 21))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=RegWin)
        self.label_12.setGeometry(QtCore.QRect(210, 370, 201, 21))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")

        self.retranslateUi(RegWin)
        QtCore.QMetaObject.connectSlotsByName(RegWin)

    def retranslateUi(self, RegWin):
        _translate = QtCore.QCoreApplication.translate
        RegWin.setWindowTitle(_translate("RegWin", "RegWin"))
        self.label_2.setText(_translate("RegWin", "Регистрация"))
        self.textEdit.setHtml(_translate("RegWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("RegWin", "<html><head/><body><p><span style=\" font-weight:600;\">ФИО</span></p></body></html>"))
        self.label_3.setText(_translate("RegWin", "<html><head/><body><p><span style=\" font-weight:600;\">Курс</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("RegWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("RegWin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Логин</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("RegWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("RegWin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Пароль</span></p></body></html>"))
        self.pushButton_2.setText(_translate("RegWin", "Зарегистрироваться"))
        self.pushButton.setToolTip(_translate("RegWin", "Вернуться назад"))
        self.pushButton.setText(_translate("RegWin", "Войти"))
        self.label_7.setText(_translate("RegWin", "<html><head/><body><p><span style=\" font-weight:600;\">Предмет</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegWin = QtWidgets.QDialog()
    ui = Ui_RegWin()
    ui.setupUi(RegWin)
    RegWin.show()
    sys.exit(app.exec())
