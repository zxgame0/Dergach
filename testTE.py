# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testTE.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 770)
        ico = QtGui.QIcon("alien.ico")
        MainWindow.setWindowIcon(ico)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(195, 449, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(9, 49, 531, 281))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 449, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(26, 420, 133, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(165, 420, 133, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 420, 133, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(9, 498, 531, 192))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 698, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 443, 131, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 698, 111, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(237, 336, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 20, 401, 20))
        self.lineEdit_4.setToolTip("")
        self.lineEdit_4.setWhatsThis("")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(438, 19, 101, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 389, 130, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 389, 122, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 400, 131, 20))
        self.label_3.setObjectName("label_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 463, 158, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Дергач"))
        self.pushButton.setText(_translate("MainWindow", "выборка"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Для получения входного текста для обработки: \n"
"1. Можно воспользоваться строкой выше, ввести URL целевой страницы.\n"
"ЛИБО\n"
"2. Скопировать необходимый текст и вставить его в это поле (в браузерах распространенная комбинация клавиш для просмотра содержимого страницы Ctrl+U, выделить все можно с помощью комбинации Ctrl+A, скопировать в буфер обмена Ctrl+С) "))
        self.pushButton_2.setText(_translate("MainWindow", "поиск"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"Здесь будет результат в случае удачного поиска по заданным критериям"))
        self.pushButton_3.setText(_translate("MainWindow", "удалить дубли"))
        self.checkBox.setText(_translate("MainWindow", "нумеровать выборку"))
        self.pushButton_5.setText(_translate("MainWindow", "очистить результат"))
        self.pushButton_6.setText(_translate("MainWindow", "очистить"))
        self.lineEdit_4.setText(_translate("MainWindow", "Введите целевой URL в эту строку"))
        self.pushButton_7.setText(_translate("MainWindow", "получить данные"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Это находится <br/><span style=\" font-weight:600;\">перед</span> искомым текстом</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Это находится <br/><span style=\" font-weight:600;\">после</span> искомого текста</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Поиск в исходном тексте</p></body></html>"))
        self.checkBox_2.setText(_translate("MainWindow", "выборка без ограничителя"))
