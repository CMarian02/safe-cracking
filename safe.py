from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import playsound

class Slider(QtWidgets.QSlider):
    def mousePressEvent(self, event):
        event.ignore()
    def wheelEvent(self, event):
        event.ignore()

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
        self.frame_dial.setGeometry(QtCore.QRect(150, 50, 550, 440))
        self.frame_dial.setText("")
        self.frame_dial.setObjectName("frame_dial")
        pixmap = QtGui.QPixmap("img/dial-frame.png")
        self.frame_dial.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_dial.setPixmap(pixmap)
        
        #Dial
        
        self.dial = QtWidgets.QLabel(self.centralwidget)
        self.dialphoto = QtGui.QPixmap("img/dial.png")
        self.dial.setGeometry(QtCore.QRect(150, 50, 550, 440))
        self.dial.setText("")
        self.dial.setObjectName("dial")
        self.dial.setAlignment(QtCore.Qt.AlignCenter)
        self.dial.setPixmap(self.dialphoto)


        #Cracker Values
        self.st_value = randint(0,360)
        self.nd_value = randint(0,360)
        self.rd_value = randint(0,360)

        #Slider

        self.slider = Slider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(130, 175, 591, 250))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slide-zone")
        self.slider.setRange(0, 360)
        self.slider.setValue(184)
        self.slider.valueChanged.connect(self.val_changed)


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Timer

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_slider_time)

        #Global Variables

        global step,value
        step = 0
        value = 184
        self.unghi = 0


        print(self.st_value)
        print(self.nd_value)
        print(self.rd_value)

    def val_changed(self):

        global step, value
        last_value = value
        value = self.slider.value()
        print(value)
        # Rotate Dial
        
        if value > last_value:
            pixmap = QtGui.QPixmap('img/dial.png')
            self.unghi = (self.unghi - 1) % 360
            transform = QtGui.QTransform().rotate(self.unghi)
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
            self.dial.setPixmap(pixmap)
            #playsound.playsound("C:/Users/gamer/Desktop/Project/safe-crack/sounds/rotate_dial.mp3")
        else:
            pixmap = QtGui.QPixmap('img/dial.png')
            self.unghi = (self.unghi + 1) % 360
            transform = QtGui.QTransform().rotate(self.unghi)
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
            self.dial.setPixmap(pixmap)

        # Verify values
                
        if value == self.st_value and step == 0:
            self.timer.setInterval(3000)
            print('here')
            self.timer.start()
        elif value == self.nd_value and step == 1:
            self.timer.setInterval(4000)
            print('here')
            self.timer.start()
        elif value == self.rd_value and step == 2:
            self.timer.setInterval(5000)
            print('here')
            self.timer.start()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SafeCracker"))
    
            
    def check_slider_time(self):
            
            global step

            if value == self.st_value and step == 0:
                self.timer.stop()
                print('done 3 secs')
                playsound.playsound("C:/Users/gamer/Desktop/Project/safe-crack/sounds/safe_click.mp3")
                step += 1
            elif value == self.nd_value and step == 1:
                self.timer.stop()
                playsound.playsound("C:/Users/gamer/Desktop/Project/safe-crack/sounds/safe_clickl.mp3")
                print('done 4 secs')
                step += 1
            elif value == self.rd_value and step == 2:
                self.timer.stop()
                print('done 5 secs')
                playsound.playsound("C:/Users/gamer/Desktop/Project/safe-crack/sounds/broke_safe.mp3")
                step += 1
                print('You Broke Safe! Good Job!')


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