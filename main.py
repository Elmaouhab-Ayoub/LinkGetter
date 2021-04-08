from googlesearch import search
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
import sys
from sys import argv
import threading
import time
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))
#ui,_ = loadUiType('main.ui')
class MainApp(QMainWindow, FORM_CLASS ):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        setup = threading.Thread(target=self.setupUi(self), args=self)
        self.ui()
        self.button()
        func = threading.Thread(target=self.searchingFun(), args=0)
        setup.start()
        func.start()


    def button(self):
        self.pushButton.clicked.connect(self.searchingFun)

    def searchingFun(self):
        time.sleep(0.1)
        # variable z is number of results
        z = self.lineEdit_2.text()
        query = self.lineEdit.text()
        try:
            z = int(z)
            search(query, tld='com', lang='en', start=0, pause=2.0)
            for result in search(query, tld="com", num=int(z), stop=int(z),pause=2) :
                self.textEdit.append(result)
        except Exception:
            pass
        

        #else :
        #    self.label_8.setText("Please enter a number")
    def ui(self):
        self.setWindowTitle("Link Getter")


def main() :
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__=="__main__" :
    main()
      