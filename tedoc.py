import sys
from testTE import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets
import collections
import re
from bs4 import BeautifulSoup
import requests

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #self.ui.pushButton_4.clicked.connect (self.putText)
        self.ui.pushButton.clicked.connect (self.vyborka)
        self.ui.pushButton_2.clicked.connect (self.findText)
        self.ui.pushButton_5.clicked.connect (self.clearRez)
        self.ui.pushButton_6.clicked.connect (self.clearRez1)
        self.ui.pushButton_3.clicked.connect (self.delDubl)
        self.ui.pushButton_7.clicked.connect (self.poluchitURL)



    def putText(self):
        pass
        #filePars = open(r"c:\Python\testur.txt", encoding="utf-8")
        #global FileChit
        #FileChit = filePars.read()
        #filePars.close()
        #self.ui.plainTextEdit.setPlainText(FileChit)

        
    def vyborka(self):  
         
       
        self.ui.plainTextEdit_2.clear()
        FileChit = self.ui.plainTextEdit.toPlainText()
        FileChit = FileChit.split('\n')
        FileChit = ''.join(FileChit)

        
        qte1 = self.ui.lineEdit.text()
        qte2 = self.ui.lineEdit_2.text()
        


        if qte1 == '' or qte2 == '':
            self.ui.plainTextEdit_2.setPlainText('не заданы ограничения')
        else:
            #проверка на запрещ символы и экранирование
            spisok_zamen = {"+": r'\+', ".": r'\.', "^": r'\^', "$": r'\$', "*": r'\*', "?": r'\?', "{": r'\{', "[": r'\[', "(": r'\(', "}": r'\}', "]": r'\]', ")": r'\)', "|": r'\|'}

            final_qte2 = list(qte2)
            for i in range(0, len(final_qte2)):
                if final_qte2[i] in spisok_zamen:
                    final_qte2[i] = spisok_zamen[final_qte2[i]]
                
            qte2 = ''.join(final_qte2)

            final_qte1 = list(qte1)
            for i in range(0, len(final_qte1)):
                if final_qte1[i] in spisok_zamen:
                    final_qte1[i] = spisok_zamen[final_qte1[i]]
                
            qte1 = ''.join(final_qte1)

            if self.ui.checkBox_2.isChecked():
                regularka = re.compile(r'' + qte1 + '.*?' + qte2 + '')
                global rez
                rez = regularka.findall(FileChit)   
                
                for i in range(0, len(rez)):
                    if self.ui.checkBox.isChecked():
                        self.ui.plainTextEdit_2.appendPlainText(str(i + 1) + ' ' + rez[i])
                    else:
                        self.ui.plainTextEdit_2.appendPlainText(rez[i])

               
                #    self.ui.plainTextEdit_2.appendPlainText('ничего не найдено - проверьте ограничители которые задаются перед и после искомого текста')
            #обработка текста
            else:
                
                regularka = re.compile(r'' + qte1 + '(.*?)' + qte2 + '')
                
                rez = regularka.findall(FileChit)
                
                
                for i in range(0, len(rez)):
                    if self.ui.checkBox.isChecked():
                        self.ui.plainTextEdit_2.appendPlainText(str(i + 1) + ' ' + rez[i])
                    else:
                        self.ui.plainTextEdit_2.appendPlainText(rez[i])
               



    def findText(self):  
        qte3 = self.ui.lineEdit_3.text()
        if qte3 != '':
            self.ui.plainTextEdit.find(qte3)


    def clearRez(self):
        self.ui.plainTextEdit_2.clear()

    def clearRez1(self):
        self.ui.plainTextEdit.clear()


    def delDubl(self):
        uniqRez = set(rez)
        self.ui.plainTextEdit_2.clear()
        for i in uniqRez:
            self.ui.plainTextEdit_2.appendPlainText(i)



    def poluchitURL(self):
        url = self.ui.lineEdit_4.text()
        try:
            result = requests.get(url)
                      
            self.ui.plainTextEdit.clear()
            soup = BeautifulSoup(result.text, "html.parser")
            htmlNutro = str(soup)
            self.ui.plainTextEdit.appendPlainText(htmlNutro)
           
          
                #self.ui.plainTextEdit.clear()
                #self.ui.plainTextEdit.appendPlainText('невозможно отобразить содержимое страницы, проверьте ее доступность в браузере')
        except:
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText('невозможно отобразить содержимое страницы, проверьте ее доступность в браузере')


         



        
      



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())