# Form implementation generated from reading ui file 'window/Add_predmet.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Add_predmetWin(object):
    def setupUi(self, Add_predmetWin):
        Add_predmetWin.setObjectName("Add_predmetWin")
        Add_predmetWin.resize(400, 170)
        self.label_3 = QtWidgets.QLabel(parent=Add_predmetWin)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 20pt \"Times New Roman\";\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_9 = QtWidgets.QPushButton(parent=Add_predmetWin)
        self.pushButton_9.setGeometry(QtCore.QRect(350, 10, 31, 31))
        self.pushButton_9.setStyleSheet("\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_2 = QtWidgets.QLabel(parent=Add_predmetWin)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 30pt \"Times New Roman\";\n"
"background-color: grey;\n"
"color: white;\n"
"text-align: center;\n"
"padding-right: 50px;\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=Add_predmetWin)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 90, 221, 41))
        self.textEdit_2.setStyleSheet(" background-color: #f6f6f6; /*Цвет текстового поля*/\n"
"  border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/\n"
" border-radius: 20px;\n"
"  border: 1px solid #2d9fd9;\n"
"  color: #a0d18c;\n"
"\n"
"  padding-left: 10px;\n"
"outline: none;\n"
"  border: 1px solid black;\n"
"  color: #2d9fd9;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(parent=Add_predmetWin)
        self.label.setGeometry(QtCore.QRect(120, 140, 221, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_9.raise_()
        self.textEdit_2.raise_()
        self.label.raise_()

        self.retranslateUi(Add_predmetWin)
        QtCore.QMetaObject.connectSlotsByName(Add_predmetWin)

    def retranslateUi(self, Add_predmetWin):
        _translate = QtCore.QCoreApplication.translate
        Add_predmetWin.setWindowTitle(_translate("Add_predmetWin", "Add_pred"))
        self.label_3.setText(_translate("Add_predmetWin", "Предмет"))
        self.pushButton_9.setToolTip(_translate("Add_predmetWin", "Добавить"))
        self.pushButton_9.setWhatsThis(_translate("Add_predmetWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rename thems</p></body></html>"))
        self.label_2.setText(_translate("Add_predmetWin", "Введите предмет"))
        self.textEdit_2.setHtml(_translate("Add_predmetWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_predmetWin = QtWidgets.QDialog()
    ui = Ui_Add_predmetWin()
    ui.setupUi(Add_predmetWin)
    Add_predmetWin.show()
    sys.exit(app.exec())
