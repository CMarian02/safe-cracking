from PyQt5 import QtWidgets, QtCore, QtGui

class WinFrame(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(550, 350)
        self.setMaximumSize(QtCore.QSize(550, 350))
        self.setMinimumSize(QtCore.QSize(550, 350))
        self.setWindowIcon(QtGui.QIcon("img/favicon.png"))
        self.win_label = QtWidgets.QLabel(self)
        self.win_label.setText('You broke safe! Congrats!')
        self.win_label.resize(550, 200)
        self.win_label.setAlignment(QtCore.Qt.AlignCenter)
        self.win_label.setObjectName("win-l")
        self.replay_button = QtWidgets.QPushButton(self)
        self.replay_button.setGeometry(175, 230, 200, 60)
        self.replay_button.setObjectName('R-button')
        self.replay_button.setText("Play Again")
        self.replay_button.clicked.connect(self.replay)
        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setGeometry(175, 290, 200, 60)
        self.exit_button.setObjectName('E-button')
        self.exit_button.setText('Exit Game')
        self.exit_button.clicked.connect(self.close_app)
    
    def replay(self):
        pass
    
    def close_app(self):
        QtWidgets.QApplication.quit()