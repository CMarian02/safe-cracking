from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsView
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
        self.frame_dial.setGeometry(QtCore.QRect(150, 50, 500, 440))
        self.frame_dial.setText("")
        self.frame_dial.setObjectName("frame_dial")
        pixmap = QtGui.QPixmap("img/dial-frame.png")
        self.frame_dial.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_dial.setPixmap(pixmap)
        
        #Dial
        
        self.dial = QtWidgets.QLabel(self.centralwidget)
        self.dialphoto = QtGui.QPixmap("img/dial.png")
        self.dial.setGeometry(QtCore.QRect(150, 50, 500, 440))
        self.dial.setText("")
        self.dial.setObjectName("dial")
        self.dial.setAlignment(QtCore.Qt.AlignCenter)
        self.dial.setPixmap(self.dialphoto)


        #Cracker Values
        self.st_value = randint(0,360)
        self.nd_value = randint(0,360)
        self.rd_value = randint(0,360)

        #Slider

        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(130, 175, 591, 250))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slide-zone")
        self.slider.setRange(0, 360)
        self.slider.setValue(184)
        self.slider.valueChanged.connect(self.val_changed)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        global step,value
        step = 0
        value = 170

        self.unghi = 0


        print(self.st_value)
        print(self.nd_value)
        print(self.rd_value)

    def val_changed(self):

        global step, value
        last_value = value
        value = self.slider.value()
        # Rotate Dial
        
        if value > last_value:
            pixmap = QtGui.QPixmap('img/dial.png')
            center = QtCore.QPoint(int(pixmap.width()/2), int(pixmap.height()/2))
            self.unghi = (self.unghi + 1) % 360
            transform = QtGui.QTransform().translate(center.x(), center.y()).rotate(self.unghi).translate(-center.x(), -center.y())
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
            pixmap = pixmap.scaled(pixmap.width(), pixmap.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            print(pixmap.size())
            pixmap_width = pixmap.width()
            pixmap_height = pixmap.height()
            dial_width = self.dial.width()
            dial_height = self.dial.height()
            pixmap_x = (dial_width - pixmap_width) / 2
            pixmap_y = (dial_height - pixmap_height) / 2
            self.dial.setGeometry(int(pixmap_x), int(pixmap_y), int(pixmap_width), int(pixmap_height))
            self.dial.setPixmap(pixmap)
        else:
            pixmap = QtGui.QPixmap('img/dial.png')
            self.unghi = (self.unghi - 1) % 360
            transform = QtGui.QTransform().rotate(self.unghi)
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
            self.dial.setPixmap(pixmap)

        # Verify values

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
