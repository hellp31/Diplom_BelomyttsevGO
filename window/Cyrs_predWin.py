# Form implementation generated from reading ui file 'window/Cyrs_predWin.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_cyrs_predWind(object):
    def setupUi(self, cyrs_predWind):
        cyrs_predWind.setObjectName("cyrs_predWind")
        cyrs_predWind.resize(497, 617)
        self.label_2 = QtWidgets.QLabel(parent=cyrs_predWind)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(-20, 0, 521, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 40pt \"Times New Roman\";\n"
"background-color: grey;\n"
"color: white;\n"
"text-align: center;\n"
"padding-right: 50px;\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_11 = QtWidgets.QPushButton(parent=cyrs_predWind)
        self.pushButton_11.setGeometry(QtCore.QRect(420, 10, 71, 81))
        self.pushButton_11.setStyleSheet(" background-color: grey; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"\n"
"  width: 250px;\n"
"  height: 30px;\n"
"outline: none;\n"
"\n"
"font-weight: bold;\n"
"font:  12pt \"Times New Roman\";\n"
"")
        self.pushButton_11.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/logout_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_3 = QtWidgets.QLabel(parent=cyrs_predWind)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(0, 110, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 40pt \"Times New Roman\";\n"
"background-color: grey;\n"
"color: white;\n"
"text-align: center;\n"
"\n"
"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=cyrs_predWind)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(260, 110, 248, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 40pt \"Times New Roman\";\n"
"background-color: grey;\n"
"color: white;\n"
"text-align: center;\n"
"\n"
"\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=cyrs_predWind)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(0, 90, 501, 95))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 40pt \"Times New Roman\";\n"
"background-color: black;\n"
"color: white;\n"
"text-align: center;\n"
"padding-right: 50px;\n"
"\n"
"")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(parent=cyrs_predWind)
        self.comboBox.setGeometry(QtCore.QRect(20, 220, 181, 61))
        self.comboBox.setStyleSheet("font: 24pt \"Times New Roman\";\n"
"\n"
"\n"
"text-align: center;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(parent=cyrs_predWind)
        self.label.setGeometry(QtCore.QRect(230, 180, 31, 441))
        self.label.setStyleSheet("background-color: black;")
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(parent=cyrs_predWind)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 220, 201, 61))
        self.comboBox_2.setStyleSheet("font: 22pt \"Times New Roman\";\n"
"\n"
"text-align: center;\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=cyrs_predWind)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 560, 121, 41))
        self.pushButton_3.setStyleSheet(" background-color: #f6f6f6; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"\n"
"  width: 250px;\n"
"  height: 30px;\n"
"\n"
"outline: none;\n"
"  border: 1px solid black;\n"
"font-weight: bold;\n"
"font:  12pt \"Times New Roman\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=cyrs_predWind)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 560, 121, 41))
        self.pushButton_4.setStyleSheet(" background-color: #f6f6f6; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"\n"
"  width: 250px;\n"
"  height: 30px;\n"
"\n"
"outline: none;\n"
"  border: 1px solid black;\n"
"font-weight: bold;\n"
"font:  12pt \"Times New Roman\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_9 = QtWidgets.QPushButton(parent=cyrs_predWind)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 430, 41, 41))
        self.pushButton_9.setToolTipDuration(0)
        self.pushButton_9.setStyleSheet(" background-color: green; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"  width: 250px;\n"
"  height: 30px;\n"
"\n"
"outline: none;\n"
"  border: 1px solid black;\n"
"font-weight: bold;\n"
"font:  12pt \"Times New Roman\";\n"
"")
        self.pushButton_9.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=cyrs_predWind)
        self.pushButton_10.setGeometry(QtCore.QRect(370, 430, 41, 41))
        self.pushButton_10.setStyleSheet(" background-color: green; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"  width: 250px;\n"
"  height: 30px;\n"
"\n"
"outline: none;\n"
"  border: 1px solid black;\n"
"font-weight: bold;\n"
"font:  12pt \"Times New Roman\";\n"
"")
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_5.raise_()
        self.label_2.raise_()
        self.pushButton_11.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.comboBox_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()

        self.retranslateUi(cyrs_predWind)
        QtCore.QMetaObject.connectSlotsByName(cyrs_predWind)

    def retranslateUi(self, cyrs_predWind):
        _translate = QtCore.QCoreApplication.translate
        cyrs_predWind.setWindowTitle(_translate("cyrs_predWind", "cyrs/predmet"))
        self.label_2.setText(_translate("cyrs_predWind", "Курсы/Предметы"))
        self.pushButton_11.setToolTip(_translate("cyrs_predWind", "Выход"))
        self.pushButton_11.setWhatsThis(_translate("cyrs_predWind", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Exit</p></body></html>"))
        self.label_3.setText(_translate("cyrs_predWind", "Курс"))
        self.label_4.setText(_translate("cyrs_predWind", "Предмет"))
        self.label.setText(_translate("cyrs_predWind", "TextLabel"))
        self.pushButton_3.setText(_translate("cyrs_predWind", "Проверить"))
        self.pushButton_4.setText(_translate("cyrs_predWind", "Сделать"))
        self.pushButton_9.setToolTip(_translate("cyrs_predWind", "Добавить курс"))
        self.pushButton_9.setWhatsThis(_translate("cyrs_predWind", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Новые курсы</p></body></html>"))
        self.pushButton_10.setToolTip(_translate("cyrs_predWind", "Добавить предмет"))
        self.pushButton_10.setWhatsThis(_translate("cyrs_predWind", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rename thems</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cyrs_predWind = QtWidgets.QDialog()
    ui = Ui_cyrs_predWind()
    ui.setupUi(cyrs_predWind)
    cyrs_predWind.show()
    sys.exit(app.exec())
