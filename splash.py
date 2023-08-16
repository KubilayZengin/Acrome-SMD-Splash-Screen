from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"color: #FFF;\n"
"}\n"
"QWidget{\n"
"background: rgb(129, 5, 5);\n"
"border-radius: 12px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.app_logo = QtWidgets.QFrame(self.centralwidget)
        self.app_logo.setMinimumSize(QtCore.QSize(0, 200))
        self.app_logo.setMaximumSize(QtCore.QSize(16777215, 300))
        self.app_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_logo.setObjectName("app_logo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.app_logo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.app_logo)
        self.label.setMinimumSize(QtCore.QSize(125, 125))
        self.label.setMaximumSize(QtCore.QSize(125, 125))
        self.label.setStyleSheet("QLabel {\n"
"background: #FFF;\n"
"border-radius: 62px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.app_logo)
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.app_description = QtWidgets.QLabel(self.background)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.app_description.setFont(font)
        self.app_description.setAlignment(QtCore.Qt.AlignCenter)
        self.app_description.setObjectName("app_description")
        self.verticalLayout_2.addWidget(self.app_description)
        self.progress = QtWidgets.QFrame(self.background)
        self.progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.progress.setObjectName("progress")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.progress)
        self.verticalLayout_3.setContentsMargins(30, 60, 30, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.percentage = QtWidgets.QLabel(self.progress)
        self.percentage.setMaximumSize(QtCore.QSize(16777215, 45))
        self.percentage.setMinimumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.percentage.setFont(font)
        self.percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage.setObjectName("percentage")
        self.verticalLayout_3.addWidget(self.percentage, 0, QtCore.Qt.AlignHCenter)
        self.progressBar = QtWidgets.QProgressBar(self.progress)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 25))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"background:rgba(255, 255, 255, 180);\n"
"border-style: none;\n"
"border-radius: 5px;\n"
"color:rgba(200, 200, 200, 0);\n"
"/*color:rgba(20, 20, 20, 0);*/\n"
"text-align:center;\n"
"}\n"
"QProgressBar::chunk {\n"
"border-radius: 5px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(66, 235, 18, 255), stop:1 rgba(255, 255, 255, 255))\n"
" \n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.progress)
        self.footer = QtWidgets.QFrame(self.background)
        self.footer.setMaximumSize(QtCore.QSize(16777215, 75))
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.author = QtWidgets.QLabel(self.footer)
        self.author.setMinimumSize(QtCore.QSize(0, 0))
        self.author.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.author.setFont(font)
        self.author.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.author.setObjectName("author")
        self.horizontalLayout_2.addWidget(self.author)
        self.verticalLayout_2.addWidget(self.footer)
        self.verticalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Logo"))
        self.label_2.setText(_translate("MainWindow", "ACROME SMD"))
        self.app_description.setText(_translate("MainWindow", "ACROME Smart Motor Driver Product family let you achieve\n"
"better precision and control over your robotics & automation projects with\n"
"enhanced productivity and performance."))
        self.percentage.setText(_translate("MainWindow", "%24"))
        self.author.setText(_translate("MainWindow", "Author: Kubilay Zengin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())