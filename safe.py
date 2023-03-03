from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 620)
        MainWindow.setMinimumSize(QtCore.QSize(920, 620))
        MainWindow.setMaximumSize(QtCore.QSize(920, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Frame Dial

        self.frame_dial = QtWidgets.QLabel(self.centralwidget)
        self.frame_dial.setGeometry(QtCore.QRect(150, 50, 570, 520))
        self.frame_dial.setText("")
        self.frame_dial.setObjectName("frame_dial")

        #Dial

        self.dial = QtWidgets.QLabel(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(146, 49, 581, 521))
        self.dial.setText("")
        self.dial.setObjectName("dial")

        #Slide Zone
        self.st_value = randint(0,200)
        self.nd_value = randint(0,200)
        self.rd_value = randint(0,200)
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(130, 200, 591, 250))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slide-zone")
        self.slider.setRange(0, 200)
        self.slider.setValue(106)
        self.slider.valueChanged.connect(self.val_changed)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        global step
        step = 0
        print(self.st_value)
        print(self.nd_value)
        print(self.rd_value)
    def val_changed(self):
        global step
        value = self.slider.value()
        print(value)
        print(step)
        if value == self.st_value and step == 0:
            print('you go to 2nd')
            step += 1
        elif value == self.nd_value and step == 1:
            print('you can go 3rd')
            step += 1
        elif value == self.rd_value and step == 2:
            print('you broke it.')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SafeCracker"))
    
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open('basic_style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
