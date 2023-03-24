from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from random import randint
from qdialog import WinFrame
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
        MainWindow.setWindowIcon(QtGui.QIcon("img/favicon.png"))
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
    
        #ProgressBar

        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(300, 500, 238, 30))
        self.progress.setValue(0)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)
        self.progress.setTextVisible(False)
    
        #Timer

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_slider_time)

        #MediaPlayer

        self.player = QMediaPlayer()
        self.file_url = QUrl.fromLocalFile('sounds/click.mp3')
        self.player.setMedia(QMediaContent(self.file_url))
        self.player_2 = QMediaPlayer()
        self.file_url_2 = QUrl.fromLocalFile('sounds/point_click.mp3')
        self.player_2.setMedia(QMediaContent(self.file_url_2))
    
        #MainWindow

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Global Variables

        global step, value, click
        click = 1
        step = 0
        value = 184
        self.unghi = 0

    #Functions for Slider

    def val_changed(self):

        global step, value, click
        last_value = value
        value = self.slider.value()
        print(value)
        print(self.st_value, self.nd_value, self.rd_value)

        # Rotate Dial
        
        if value > last_value:
            pixmap = QtGui.QPixmap('img/dial.png')
            self.unghi = (self.unghi - 1) % 360
            transform = QtGui.QTransform().rotate(self.unghi)
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
            self.dial.setPixmap(pixmap)
            if click % 2 == 0 and value != [self.st_value, self.nd_value, self.rd_value]:
                self.player.play()
            click += 1
        else:
            pixmap = QtGui.QPixmap('img/dial.png')
            self.unghi = (self.unghi + 1) % 360
            transform = QtGui.QTransform().rotate(self.unghi)
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
            self.dial.setPixmap(pixmap)
            if click % 2 == 0 and value != [self.st_value, self.nd_value, self.rd_value]:
                self.player.play()
            click +=1

        # Verify values
                
        if value == self.st_value and step == 0:
            self.player_2.play()
            self.timer.setInterval(3000)
            print('here')
            self.timer.start()
        elif value == self.nd_value and step == 1:
            self.player_2.play()
            self.timer.setInterval(4000)
            print('here')
            self.timer.start()
        elif value == self.rd_value and step == 2:
            self.player_2.play()
            self.timer.setInterval(5000)
            print('here')
            self.timer.start()
        
        #Change ProgressBar procent

        if step == 0:
            self.check_progress(value, self.st_value)
        elif step == 1:
            self.check_progress(value, self.nd_value)
        elif step == 2:
            self.check_progress(value, self.rd_value)

    #Create ProgressBar chunks

    def check_progress(self, value, step):
        if (step - value) > 250 and (step - value) <= 360 or ((value - step) > 250 and (value - step) <= 360):
            self.progress.setValue(0)
        elif (step - value) > 150 and (step - value) <= 250 or ((value - step) > 150 and (value - step) <= 250):
            self.progress.setValue(20)
            self.progress.setStyleSheet('''QProgressBar::chunk{
            background-color:green;
            }''')
        elif (step - value) > 50 and (step - value) <= 150 or ((value - step) > 50 and (value - step) <= 150):
            self.progress.setValue(40)
            self.progress.setStyleSheet('''QProgressBar::chunk{
            background-color:yellow;
            }''')
        elif (step - value) > 10 and (step - value) <= 50 or ((value - step) > 10 and (value - step) <= 50):
            self.progress.setValue(60)
            self.progress.setStyleSheet('''QProgressBar::chunk{
            background-color:orange╚;
            }''')
        elif (step - value) > 5 and (step - value) <= 10 or ((value - step) > 5 and (value - step) <= 10):
            self.progress.setValue(80)
            self.progress.setStyleSheet('''QProgressBar::chunk{
            background-color:orange;
            }''')
        elif (step - value) >= 0 and (step - value) <= 5 or ((value -step) >= 0 and (value - step) <= 5):
            self.progress.setValue(100)
            self.progress.setStyleSheet('''QProgressBar::chunk{
            background-color:red;
            }''')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SafeCracker"))
    
    #Check if slider stay on good value for 3 sec

    def check_slider_time(self):
            
            global step

            if value == self.st_value and step == 0:
                self.timer.stop()
                print('done 3 secs')
                playsound.playsound("C:/Users/gamer/OneDrive/Desktop/Projects/safe-cracking/sounds/safe_click.mp3")
                step += 1
                self.check_progress(value, self.nd_value)
            elif value == self.nd_value and step == 1:
                self.timer.stop()
                playsound.playsound("C:/Users/gamer/OneDrive/Desktop/Projects/safe-cracking/sounds/safe_clickl.mp3")
                print('done 4 secs')
                step += 1
                self.check_progress(value, self.rd_value)
            elif value == self.rd_value and step == 2:
                self.timer.stop()
                print('done 5 secs')
                playsound.playsound("C:/Users/gamer/OneDrive/Desktop/Projects/safe-cracking/sounds/broke_safe.mp3")
                step += 1
                self.open_frame()
                print('You Broke Safe! Good Job!')

    def open_frame(self):
        frame = WinFrame()
        frame.setWindowTitle('You Win')
        with open('basic_style.css', 'r') as f:
            stylesheet = f.read()
        frame.setStyleSheet(stylesheet)
        frame.exec_()

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
