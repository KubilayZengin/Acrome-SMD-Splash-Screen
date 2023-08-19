import sys

# PyQt5 modüllerini içe aktarıyoruz
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QMessageBox
from PyQt5.QtCore import QSettings

# Import Splash screen UI ve Main Window UI
from splash import Ui_SplashScreen
from SMD_qt import Ui_MainWindow

# Globals: Programın farklı kısımlarında kullanılacak global değişkenler
counter = 0  # Animasyon ilerlemesi için sayaç


# Ana pencere
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_to_screen()  # Pencereyi ekran merkezine taşı
        self.ui.pushButton_56.clicked.connect(self.login)  # Butona tıklama işlemini fonksiyonla bağla
        self.load_settings()  # Önceden kaydedilen verileri yükle

    def login(self):
        # Boş bir liste oluştur
        data = []
        for i in range(25, 34):
            # Her lineEdit'in metnini listeye ekle
            data.append(getattr(self.ui, f'lineEdit_{i}').text())
        self.save_settings(*data)  # Verileri kaydet

    def save_settings(self, *data):
        settings = QSettings("MyCompany", "MyApp")
        for i, value in enumerate(data):
            key = f"data{i + 1}"
            settings.setValue(key, value)
        self.message("Data has been saved successfully.", QMessageBox.Information)  # Bilgi mesajı göster

    def load_settings(self):
        settings = QSettings("MyCompany", "MyApp")
        for i in range(1, 10):
            key = f"data{i}"
            value = settings.value(key)
            if value is not None:
                getattr(self.ui, f'lineEdit_{i + 24}').setText(value)  # Verileri yükle ve lineEdit'e yaz

    # Pencereyi ekranda merkeze taşıma fonksiyonu
    def center_to_screen(self):
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    # MessageBox oluşturma fonksiyonu
    def message(self, text, msg_type):  # Parametreler: Yazdırılacak mesaj, Mesajın türü
        msg = QMessageBox()  # Bir QMessageBox örneği oluştur
        msg.setWindowTitle("Attention")  # Başlık
        msg.setText(text)  # Metin içeriği
        msg.setIcon(msg_type)  # Mesaj tipini belirle
        x = msg.exec_()  # Mesajı göster


# Splash penceresi
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.center_to_screen()

        # Başlık çubuğunu kaldır
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Acrome logosunu ayarla
        pixmap = QtGui.QPixmap('images/acromelogo.png')
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setScaledContents(True)
        self.ui.label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        # Arkaplanı gizle
        self.ui.background.setMaximumHeight(0)

        # Animasyonları başlat
        self.logo_animation()
        self.description_animation()
        self.start_animation()

        # Qtimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(25)  # Timer'ı başlat

    # Logo animasyonunu oluştur
    def logo_animation(self):
        opacity_effect = QtWidgets.QGraphicsOpacityEffect(self.ui.label)
        self.ui.label.setGraphicsEffect(opacity_effect)

        self.logo_opacity_animation = QtCore.QPropertyAnimation(
            opacity_effect, b'opacity', duration=1500, startValue=0, endValue=1)
        self.logo_opacity_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)

    # Açıklama animasyonunu oluştur
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

    # Animasyonları başlat
    def start_animation(self):
        self.anim_group = QtCore.QParallelAnimationGroup(self.ui.background)
        self.anim_group.addAnimation(self.logo_opacity_animation)
        self.anim_group.addAnimation(self.description_animation)
        self.anim_group.start()

    # İlerleme çubuğu yüklenmesi
    def progress(self):
        global counter
        self.ui.progressBar.setValue(int(counter))  # İlerleme çubuğunun değerini ayarla
        self.ui.percentage.setText(f"{int(counter)}%")  # Yüzde değerini ayarla

        if counter >= 100:  # İlerleme 100'e ulaştığında
            self.timer.stop()  # Zamanlayıcıyı durdur
            self.main = MainWindow()  # Ana pencereyi oluştur
            self.main.show()  # Ana pencereyi göster
            self.close()  # Splash penceresini kapat
        counter += 0.5  # Sayaç değerini artır (arttırılabilir ya da azaltılabilir)

    def center_to_screen(self):
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())  # Pencereyi ekranda merkeze taşı


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()  # Splash penceresini oluştur
    window.show()  # Splash penceresini göster
    sys.exit(app.exec_())  # Uygulamayı başlat
