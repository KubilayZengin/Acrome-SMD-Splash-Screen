import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
# Import splash screen UI
from splash import Ui_SplashScreen
# Import main screen UI
from SMD_qt import Ui_MainWindow

# Globals
counter = 0


# Main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_to_screen()

    def center_to_screen(self):
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())


# Splash window
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.center_to_screen()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set Acrome's Logo
        pixmap = QtGui.QPixmap('images/acromelogo.png')
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setScaledContents(True)
        self.ui.label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        # Hide Background
        self.ui.background.setMaximumHeight(0)

        # Initialize animation
        self.logo_animation()
        self.description_animation()
        self.start_animation()

        # Qtimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # Timer in milliseconds
        self.timer.start(25)

    # Animate logo function
    def logo_animation(self):
        opacity_effect = QtWidgets.QGraphicsOpacityEffect(self.ui.label)
        self.ui.label.setGraphicsEffect(opacity_effect)

        # noinspection PyArgumentList
        self.logo_opacity_animation = QtCore.QPropertyAnimation(
            # Parameters respectively: object, property of the widget, duration in ms, start, end
            opacity_effect, b'opacity', duration=1500, startValue=0, endValue=1)
        self.logo_opacity_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)

    # Animate description function
    def description_animation(self):
        opacity_effect = QtWidgets.QGraphicsOpacityEffect(self.ui.background)
        self.ui.background.setGraphicsEffect(opacity_effect)

        geometry_animation = QtCore.QPropertyAnimation(
            self.ui.background,
            b'maximumHeight',
            duration=1000,
            startValue=0,
            endValue=228,
        )
        geometry_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        opacity_animation = QtCore.QPropertyAnimation(
            opacity_effect, b'opacity', duration=500, startValue=0, endValue=1)
        self.description_animation = QtCore.QParallelAnimationGroup(self.ui.background)
        self.description_animation.addAnimation(geometry_animation)
        self.description_animation.addAnimation(opacity_animation)

    # Start Animation
    def start_animation(self):
        self.anim_group = QtCore.QParallelAnimationGroup(self.ui.background)
        self.anim_group.addAnimation(self.logo_opacity_animation)
        self.anim_group.addAnimation(self.description_animation)
        self.anim_group.start()

    # Progress Function
    def progress(self):
        global counter
        # Set value to progress bar
        self.ui.progressBar.setValue(int(counter))
        self.ui.percentage.setText(f"{int(counter)}%")

        # Close splash screen and open app
        if counter >= 100:
            # Stop timer
            self.timer.stop()
            # Show main windows
            self.main = MainWindow()
            self.main.show()
            # Close splash screen
            self.close()
        # Increase counter +=0.5
        counter += 0.5

    def center_to_screen(self):
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()
    window.show()
    sys.exit(app.exec_())
